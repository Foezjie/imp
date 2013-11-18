.. vim: spell

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

In the remainder of this chaper we will install the framework but use on a
single machine.

.. note::

   Currently only Fedora is supported, both in the deployment agent and the
   configuration modules. Because IMP is a tool to manage systems and their
   configuration, we recommend to start with IMP on a virtual machine to ensure
   that your current machine keeps working as expected. This guide has been tested
   on a Fedora 18 virtual machine.

.. warning::

   DO NOT run this guide on your own machine, or it will be reconfigured.
   Use a fedora 18 VM, with hostname vm1 to be fully compatible with this guide.

Installing IMP
==============

The source of IMP is available on GitHub at https://github.com/bartv/imp
On Fedora run the following commands to install dependencies, the python3 runtime
and checking out imp and installing it.

.. code-block:: sh

   yum install -y python3-setuptools python3-amqplib python3-tornado \
         python3-dateutil python3-plyvel python3-execnet git
   git clone https://github.com/bartv/imp
   cd imp
   python3 setup.py install


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

The configuration file defines that re-usable modules are stored in ``libs``
and when the configuration model is compiled, the imp-agent export plug-in needs
to be called.

The IMP compiler looks for a file called ``main.cf`` to start the compilation from.
The last line, creates an empty file.

In the next section we will re-use existing modules to deploy our LAMP stack.

Re-use existing modules
=======================

At github many modules are already hosted that provide a meta-model with
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
this guide we assume that drupal will be installed on a server called ``vm1``.

Compose a configuration model
-----------------------------

The modules we installed in the previous section encapsulate the configuration
required for certain services or subsystems. In this section we will make
a 'composition' of the configuration modules to deploy and configure a Drupal
website. This composition needs to be put in the main.cf file.

.. code-block:: ruby
   :linenos:

   # define the machine we want to deploy Drupal on
   vm1 = ip::Host(name = "vm1", os = "fedora-18", ip = "172.16.1.3")

   # add a mysql and apache http server
   web_server = httpd::Server(host = vm1)
   mysql_server = mysql::Server(host = vm1)

   # define a new virtual host to deploy drupal in
   vhost_name = httpd::VhostName(name = "localhost")
   vhost = httpd::Vhost(webserver = web_server, name = vhost_name,
      document_root = "/var/www/html/drupal_test")

   # deploy drupal in that virtual host
   drupal::Common(host = vm1)
   db = mysql::Database(server = mysql_server, name = "drupal_test",
      user = "drupal_test", password = "Str0ng-P433w0rd")
   drupal::Site(vhost = vhost, database = db)

On line 2 we define the server on which we want to deploy Drupal. The name is
the hostname of the machine, which is later used to determine what
configuration needs to be deployed on which machine. The os attribute defines
what operating system this server runs. This attribute can be used to create
configuration modules that handle the heterogienity of different operating
systems. The ip attribute is the ipaddress of this host. In this introduction
we define this attirbute manually, later on we will let IMP manage this
automatically.

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


Making it work
--------------

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


Accessing your new Drupal install
---------------------------------

Use ssh port-forwarding to forward port 80 on vm1 to your local machine, to
port 2080 for example (ssh -L 2080:localhost:80 ec2-user@172.16.1.3). This allows you to surf to
http://localhost:2080/

.. warning::

   Using "localhost" in the url is essential because the configuration model
   generates a named based virtual host that matches the name *localhost*.

On the first access the database will not have been initialised. Surf to
http://localhost:2080/install.php

The database has already been configured and Drupal should skip this setup to
the point where you can configure details such as the admin user.

.. note::

   Windows users can use putty for ssh access to their servers. Putty also
   allows port forwarding. You can find more information on this topic here:
   http://the.earth.li/~sgtatham/putty/0.63/htmldoc/Chapter3.html#using-port-forwarding


Managing multiple machines
==========================

The real power of IMP appears when you want to manage more than one machine. In
this section we will move the mysql server from vm1 to a second virtual machine
called vm2. We will still manage this additional machine in ``single shot``
mode using a remote deploy.

SSH setup
---------

The remote deploy feature uses an ssh connection to the target host to deploy
changes to that host. Additionally the remote deploy command requires the name
used in the configuration model and not the ip which you would use to connect to
the host (in the absence of a configured DNS server).

.. code-block:: sh
    :linenos:

    ssh-keygen -t rsa
    cat /root/.ssh/id_rsa.pub
    ssh-rsa AAAAB3NzaC1yc...Poid94ZA0kZQ229wCxwtIERI8EFGyJa1BFd9t8wYlT3/J+uSzAfifN+sjPL root@vm1


First as root generate a new ssh key on vm1 with ssh-keygen (on line 1). This command will
ask you where to store the key and whether you want to set a passphrase on this
key. Use the default location and do not set a password (For this simple demo in
throw away virtual machines this increased security is not required). Output
this key to the terminal with the command on line 2 and copy its output. The
output will be a base64 encoded string that starts with ssh-rsa and ends with
something like what is shown on line 3.

.. code-block:: sh
    :linenos:

    echo "ssh-rsa AAAAB3NzaC1yc...Poid94ZA0kZQ229wCxwtIERI8EFGyJa1BFd9t8wYlT3/J+uSzAfifN+sjPL root@vm1" >> /root/.ssh/authorized_keys

Append the public key be appending it to /root/.ssh/authorized_keys on vm2. You
can achieve this by pasting the copied key content between quotes and appending
it to that file, as shown on line 1.

The IMP remote deploy command takes the name of the remote host. This name
should match the name in the configuration model and is used to access the
remote host. Because the names of the virtual machines are not configured in DNS
we need to configure and alias in the ssh configuration.

Add the following to /root/.ssh/authorized_keys

.. code-block:: sh

    Host vm2
        Hostname 172.16.1.4


vm2 preparation
---------------

On vm2 we also need to open up the firewall for the services that it will host.
On this virtual machine this is port 3306/tcp for mysql.

.. code-block:: sh

   firewall-cmd --permanent --zone=public --add-port=3306/tcp


Update the configuration model
------------------------------

A second virtual machine is easily added to the system by adding the definition
of the virtual machine to the configuration model and assigning the mysql server
to the new virtual machine.

.. code-block:: ruby
   :linenos:

   # define the machine we want to deploy Drupal on
   vm1 = ip::Host(name = "vm1", os = "fedora-18", ip = "172.16.1.3")
   vm2 = ip::Host(name = "vm2", os = "fedora-18", ip = "172.16.1.4")

   # add a mysql and apache http server
   web_server = httpd::Server(host = vm1)
   mysql_server = mysql::Server(host = vm2)

   # define a new virtual host to deploy drupal in
   vhost_name = httpd::VhostName(name = "localhost")
   vhost = httpd::Vhost(webserver = web_server, name = vhost_name,
      document_root = "/var/www/html/drupal_test")

   # deploy drupal in that virtual host
   drupal::Common(host = vm1)
   db = mysql::Database(server = mysql_server, name = "drupal_test",
      user = "drupal_test", password = "Str0ng-P433w0rd")
   drupal::Site(vhost = vhost, database = db)

On line 3 the definition of the new virtual machine is added. On line 7 the
mysql server is assigned to vm2.

Deploy the configuration model
------------------------------

Deploy the new configuration model by invoking a local deploy on vm1 and a
remote deploy on vm2.

.. code-block:: sh

    imp deploy
    imp deploy -r vm2


Create your own modules
=======================

IMP enables developers of a configuration model to make it modular and
reusable. In this section we create a configuration module that defines how to
deploy a LAMP stack with a Drupal site in a two or three tiered deployment.

Module layout
-------------
A configuration module requires a specific layout:

    * The name of the module is determined by the top-level directory. In this
      directory the only required directory is the ``model`` directory with a file
      called _init.cf.
    * What is defined in the main.cf file is available in the namespace linked with
      the name of the module. Other files in the model directory create subnamespaces.
    * The files directory contains files that are deployed verbatim to managed
      machines
    * The templates directory contains templates that use parameters from the
      configuration model to generate configuration files.
    * Python files in the plugins directory are loaded by the platform and can
      extend it using the IMP API.


.. code-block:: sh

    module
    |__ files
    |    |__ file1.txt
    |
    |__ model
    |    |__ _init.cf
    |    |__ services.cf
    |
    |__ plugins
    |    |__ functions.py
    |
    |__ templates
         |__ conf_file.conf.tmpl


We will create our custom module in the ``libs`` directory of the quickstart
project. Our new module will call ``lamp`` and only the _init.cf file is really
required. The following commands create all directories to develop a
full-featured module.

.. code-block:: sh

    cd /root/quickstart/libs
    mkdir {lamp,lamp/model}
    touch lamp/model/_init.cf

    mkdir {lamp/files,lamp/templates}
    mkdir lamp/plugins


Configuration model
-------------------

In lamp/model/_init.cf we define the configuration model that defines the lamp
configuration module.

.. code-block:: ruby
    :linenos:

    entity DrupalStack:
        string stack_id
        string vhostname
    end

    index DrupalStack(stack_id)

    ip::Host webserver [1] -- [0:1] DrupalStack drupal_stack_webserver
    ip::Host mysqlserver [1] -- [0:1] DrupalStack drupal_stack_mysqlserver

    implementation drupalStackImplementation:
        # add a mysql and apache http server
        web = httpd::Server(host = webserver)
        mysql = mysql::Server(host = mysqlserver)

        # define a new virtual host to deploy drupal in
        vhost_name = httpd::VhostName(name = vhostname)
        vhost = httpd::Vhost(webserver = web, name = vhost_name,
                document_root = "/var/www/html/{{ stack_id }}")

        # deploy drupal in that virtual host
        drupal::Common(host = webserver)
        db = mysql::Database(server = mysql, name = stack_id,
                user = stack_id, password = "Str0ng-P433w0rd")
        drupal::Site(vhost = vhost, database = db)
    end

    implement DrupalStack using drupalStackImplementation

On line 1 to 4 we define an entity which is the definition of a ``concept`` in
the configuration model. Entities behave as an interface to a partial
configuration model that encapsulates parts of the configuration, in this case
how to configure a LAMP stack. On line 2 and 3 typed attributes are defined
which we can later on use in the implementation of an entity instance.

Line 6 defines that stack_id is an identifying attribute for instances of
the DrupalStack entity. This also means that all instances of DrupalStack need
to have a unique stack_id attribute.

On lines 8 and 9 we define a relation between a Host and our DrupalStack entity.
This relation represents a double binding between these instances and it has a
multiplicity. The first relations reads as following:

    * Each DrupalStack instance has exactly one ip::Host instance that is stored
      in the webserver attribute.
    * Each ip::Host has zero or one DrupalStack instances that use the host as a
      webserver. The DrupalStack instance is stored in the
      drupal_stack_webserver attribute.

.. warning::

   On line 8 and 9 we explicity give the DrupalStack side of the relation a
   multiplicity that starts from zero. Setting this to one would break the ip
   module because each Host would require an instance of DrupalStack.

On line 11 to 26 an implementation is defined that provides a refinement of the DrupalStack entity.
It encapsulates the configuration of a LAMP stack behind the interface of the entity by defining
DrupalStack in function of other entities, which on their turn do the same. The refinement process
is evaluated by the compiler and continues until all instances are refined into instances of
entities that IMP knows how to deploy.

Inside the implementation the attributes and relations of the entity are available as variables.
They can be hidden by new variable definitions, but are also accessible through the ``self``
variable (not used in this example). On line 19 an attribute is used in an inline template with the
{{ }} syntax.

And finally on line 28 we link the implementation to the entity itself.

The composition
---------------

With our new LAMP module we can reduce the amount of required configuration code in the main.cf file
by using more ``reusable`` configure code. Only three lines of site specific configuration code are
left.

.. code-block:: ruby
    :linenos:

    # define the machine we want to deploy Drupal on
    vm1 = ip::Host(name = "vm1", os = "fedora-18", ip = "172.16.1.3")
    vm2 = ip::Host(name = "vm2", os = "fedora-18", ip = "172.16.1.4")

    lamp::DrupalStack(webserver = vm1, mysqlserver = vm2,
        stack_id = "drupal_test", vhostname = "localhost")

Deploy the changes
------------------

Deploy the changes as before and nothing should change because it generates exactly the same
configuration.

.. code-block:: sh

    imp deploy
    imp deploy -r vm2

Deploy a file
-------------

Until know we only used high level concepts in the new configuration module. In this section we will
add an additional implementation (that is also always selected) and installs a customized message of
the day file on each of the virtual machines.

.. code-block:: ruby
    :linenos:

    implementation stackMotd:
        std::File(host = webserver, path = “/etc/motd”, owner = “root”,
            group = “root”, group = “root”, mode = 644,
            content = template(“lamp/motd.tmpl”))

        std::File(host = mysqlserver, path = “/etc/motd”, owner = “root”,
            group = “root”, group = “root”, mode = 644,
            content = template(“lamp/motd.tmpl”))
    end

    implement DrupalStack using stackMotd


Using a central server
======================

The deploy and remote deploy commands become cumbersome when multiple hosts need to be managed.
Especially when dependencies exists between managed hosts. In this section we will configure vm1 as
the management server for our small infrastructure. On this machine we will install a RabbitMQ AMQP
server, the IMP management server and the IMP agent. On all other virtual machines only the IMP
agent is required.


