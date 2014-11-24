Summary: Scripts for managing a Highly Available CVMFS Stratum1 pair of machines
Name: cvmfs-hastratum1
Version: 1.3
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
* Mon Nov 24 2014 Dave Dykstra <dwd@fnal.gov> 1.3-1
- also set a PATH in remove-repository and add-repository to find kinit,
    in case they are run from cron

* Fri Nov 21 2014 Dave Dykstra <dwd@fnal.gov> 1.2-1
- add -f option to remove-repository command to skip asking for confirmation

* Thu Oct 16 2014 Dave Dykstra <dwd@fnal.gov> 1.1-1
- fix a couple of kerberos-related things: set missing $THISHOST in
    remove-repository, and set a PATH in pull_and_push to find kinit
    (since cron doesn't set the PATH).

* Thu Oct 10 2014 Dave Dykstra <dwd@fnal.gov> 1.0-1
- Initial release
