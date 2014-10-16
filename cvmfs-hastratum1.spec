Summary: Scripts for managing a Highly Available CVMFS Stratum1 pair of machines
Name: cvmfs-hastratum1
Version: 1.1
Release: 1
Group: Applications/System
License: BSD
Source: http://frontier.cern.ch/dist/cvmfs-hastratum1-%{version}.tgz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
Requires: cvmfs-server
Requires: heartbeat

%description
%{summary}

%prep
%setup

%install
[[ %{buildroot} != / ]] && rm -rf %{buildroot}
ls
make PREFIX=%{buildroot} install

%clean
[[ %{buildroot} != / ]] && rm -rf %{buildroot}

%files
/usr/sbin/*
/etc/ha.d/*.in
/etc/ha.d/resource.d/*
/etc/cvmfs/*
/etc/logrotate.d/*

%changelog
* Thu Oct 16 2014 Dave Dykstra <dwd@fnal.gov> 1.1-1
- set missing $THISHOST in remove-repository

* Thu Oct 10 2014 Dave Dykstra <dwd@fnal.gov> 1.0-1
- Initial release
