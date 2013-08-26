Getting started
***************

This chapter gives a short introduction to IMP. It provides the basics to
get started with IMP:

   * Install IMP
   * Create an IMP project
   * Use existing configuration modules
   * Create a configuration model to deploy a LAMP (Linux, Apache, Mysql and PHP) stack
   * Deploy the configuration
   
The remainder of the documentation goes further into the architecture, the
configuration model, language reference and the framework API.

The framework exists of several components:

   * A stateless compiler that builds the configuration model
   * The central IMP server that stores states
   * IMP agents on each managed system that deploy configuration changes.
   
In this section we will install the entire framework but only use the compiler
with an embeded agent to deploy configuration changes. 

*Currently only Fedora is supported, both in the deployment agent and the 
configuration modules.*

*Because IMP is a tool to manage systems and their configuration, we recommand
to start with IMP on a virtual machine to ensure that your current machine 
keeps working as expected.*

TODO: Virtual machine image download 
   
Installing IMP
==============

The source of IMP is available on GitHub at https://github.com/bartv/imp
The Readme in the IMP code repository contains the infrastructions for
checking out the code and installing it on your machine.

Create an IMP project
=====================

An IMP project bundles modules that contain configuration information. A project
is nothing more than a directory with an .imp file, which contains parameters
such as the location to search for modules and where to find the server.

Here we will create a directory ``quickstart`` with a basic configuration file.

.. code-block:: sh
   
   mkdir quickstart
   cd quickstart
   cat > .imp <<EOF
   [config]
   lib-dir = libs
   export = imp-agent
   EOF
   mkdir libs
   touch main.cf

The configuration file defines that the library with modules is stored in ``libs``
and when the configuration model is compiled, the imp-agent export plugin needs
to be called. Additionally the compiler will look for a file called ``main.cf`` 
to start the compilation from.

In the next section we will re-use existing modules to deploy our LAMP stack.

Re-use existing modules
=======================

At github many modules are already hosted that provide at least a meta-model with
configuration concepts and often an implementation for one or more operating
systems. Our modules are available in the https://github.com/bartv/imp-* repositories.


In the previous section we configured the project to use the imp-agent for 
deployment. This agent knows how to deploy and configure File, Directories,
Services and Packages. The ``std`` module defines these concepts and therefore
it is the first package we need.

.. code-block:: sh
   
   cd libs
   git clone https://github.com/bartv/imp-std.git std
   
For the LAMP stack we need modules that provide basic functionality
such as networking (``net`` and ``ip``) and support for redhat based operating systems
(``redhat``). Addionally also the modules that configure the Apache webserver
and a Mysql server (``apache``, ``httpd``, and ``mysql``). And finally
a module to configure PHP and Drupal (``php`` and ``drupal``).

.. code-block:: sh

   for mod in net ip redhat httpd mysql apache php drupal; do
       git clone https://github.com/bartv/imp-$mod.git $mod
   done

We now have all configuration modules required to deploy Drupal on a LAMP stack. 

The configuration model
=======================

In this section we will use the configuration concepts defined in the existing
modules to create new composition that defines the final configuration model. In
this guid we assume that drupal will be installed on a server called ``vm1``.

Compose a configuration model
-----------------------------

The modules we installed in the previous section encapsulate the configuration
required for certain services or subsystems. In this section we will make
a 'composition' of the configuration modules to deploy and configure a Drupal
website.

.. code-block:: ruby
   :linenos:

   # define the machine we want to deploy Drupal on
   server = std::Host(name = "vm1", os = "fedora-18")
   
   # add a mysql and apache http server
   web_server = httpd::Server(host = server)
   mysql_server = mysql::Server(host = server)
   
   # define a new virtual host to deploy drupal in
   vhost_name = httpd::VhostName(name = "localhost")
   vhost = httpd::Vhost(webserver = web_server, name = vhost_name, 
      document_root = "/var/www/html/drupal-test")
   
   # deploy drupal in that virtual host
   drupal::Common(host = server)
   db = mysql::Database(server = mysql_server, name = "drupal_test", 
      user = "drupal_test", password = "Str0ng-P433w0rd")
   drupal::Site(vhost = vhost, database = db)
 
On line 2 we define the server on which we want to deploy Drupal. The name 
is the hostname of the machine, which is later used to determine what configuration
needs to be deployed on which machine. The os attribute defines what operating
system this server runs. This attribute can be used to create configuration
modules that handle the heterogienity of different operating systems.

Lines 5 and 6 deploy an httpd server and mysql server on our server.

Lines 9 to 11 define a virtual host in which we want to deploy our Drupal 
website.

Line 14 deploys common Drupal configuration on our server and line 17 creates
a Drupal site on the virtual host we defined previously.

Line 16 defines a database for our Drupal website.


Deploy the configuration model
------------------------------

The normal mode of operation of IMP is in a setting where each managed host runs
a configuration agent that is receives configuration updates from a central
server. This setup is quite elaborate and in this introduction we will use the
single shot *deploy* command. This command compiles, exports and enforces the 
configuration of the server it is executed on.

The configuration mode we made in the previous section can be deployed by 
executing the deploy command in the IMP project.

.. code-block:: sh

   imp deploy


Accessing your new Drupal install
---------------------------------

Use ssh port-forwarding to forward port 80 on vm1 to your local machine, to
port 2080 for example (ssh -L 2080:localhost:80). This allows you to surf to http://localhost:2080/ This is
essential because the configuration model generates a named based virtual host 
that matches the name *localhost*.

On the first access the database will not have been initialised. Surf to
http://localhost:2080/install.php

The database has already been configured and Drupal should skip this setup to
the point where you can configure details such as the admin user.
 

Remarks
-------

In a default fedora SELinux and the firewall are configured. This may cause
problems because managing these services is not covered here. We recommend that
you either set SELinux to permissive mode and disable the firewall with:

.. code-block:: sh

   setenforce 0
   sed -i "s/SELINUX=enforcing/SELINUX=permissive/g" /etc/sysconfig/selinux
   systemctl stop firewalld
   
Or allow apache to connect to the network and open up port 80 in the firewall.

.. code-block:: sh

   setsebool httpd_can_network_connect true
   firewall-cmd --permanent --zone=public --add-service=http
   

