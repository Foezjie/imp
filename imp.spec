Name:           python-imp
Version:        0.10.0
Release:        1%{?dist}
Summary:        Infrastructure management platform

Group:          Development/Languages
License:        LGPLv2+
URL:            http://distrinet.cs.kuleuven.be
Source0:        http://distrinet.cs.kuleuven.be/imp-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
#%if 0%{?rhel}
#%%endif

#%if 0%{?fedora} >= 4
#%endif

%if 0%{?fedora} >= 17
BuildRequires:  systemd
%endif

Requires:       python3
Requires:       python3-amqplib
Requires:       python3-tornado
Requires:       python3-dateutil
Requires:       python3-execnet
Requires:       python3-apsw

Requires(pre):  shadow-utils

%description

%prep
%setup -q -n imp-%{version}

%build
%{__python3} setup.py build


%install
rm -rf %{buildroot}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
chmod -x LICENSE
mkdir -p %{buildroot}%{_localstatedir}/lib/imp
mkdir -p %{buildroot}%{_localstatedir}/lib/imp/fileserver
mkdir -p %{buildroot}/etc/imp
mkdir -p %{buildroot}%{_localstatedir}/log/imp
install -m 644 misc/imp.cfg %{buildroot}/etc/imp/example.cfg
%if 0%{?fedora} >= 17
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 misc/imp-agent.service $RPM_BUILD_ROOT%{_unitdir}/imp-agent.service
install -p -m 644 misc/imp-server.service $RPM_BUILD_ROOT%{_unitdir}/imp-server.service
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE docs/*
%{python3_sitelib}/imp-%{version}-py?.?.egg-info
%{python3_sitelib}/Imp
%{_bindir}/imp
%attr(-, imp, imp) %{_localstatedir}/lib/imp
%config %attr(-, imp, imp) /etc/imp/*
%attr(-, imp, imp) %{_localstatedir}/log/imp
%if 0%{?fedora} >= 17
%attr(-,root,root) %{_unitdir}/*.service
%endif

%if 0%{?fedora} >= 17
%post
%systemd_post imp-agent.service

%preun
%systemd_preun imp-server.service

%postun
%systemd_postun_with_restart imp-server.service

%endif

%pre
getent group imp >/dev/null || groupadd -r imp
getent passwd imp >/dev/null || \
    useradd -r -g imp -d /var/lib/imp -s /bin/bash \
    -c "Account used by the IMP daemons" imp
exit

%changelog
* Tue Nov 13 2012 Bart Vanbrabant <bart.vanbrabant@cs.kuleuven.be> - 0.2-1
- Initial release

