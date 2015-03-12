Summary: Scripts for managing a Highly Available CVMFS Stratum1 pair of machines
Name: cvmfs-hastratum1
Version: 1.7
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
* Thu Mar 12 2015 Dave Dykstra <dwd@fnal.gov> 1.7-1
- Always have the /var/spool/cvmfs/<repo>/tmp symlink point to $STORAGE
  so it's one less thing to do when moving a repo from one $SRV to another.

* Thu Feb 26 2015 Dave Dykstra <dwd@fnal.gov> 1.6-1
- add a "continue" option to add-repository to do just the snapshot
  part, in case the initial snapshot fails

* Thu Feb 12 2015 Dave Dykstra <dwd@fnal.gov> 1.5-1
- have pull_and_push also append /stage to CVMFS_STRATUM1 on the backup
  host if it isn't there.

* Wed Feb 11 2015 Dave Dykstra <dwd@fnal.gov> 1.4-1
- have add-repository and pull_and_push edit the new $CVMFS_STRATUM1 URL
  put in server.conf by cvmfs-server 2.1.20, to point to the stage
  subdirectory
- change pull_and_push to accept single repository name to update instead
  of all repositories
- change add-repository to support keys directly in /etc/cvmfs/keys or
  in /etc/cvmfs/keys/<domain> directories
- change add-repository to add optional $EXTRAKEYS to added repository
  if they're not already in the default

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
