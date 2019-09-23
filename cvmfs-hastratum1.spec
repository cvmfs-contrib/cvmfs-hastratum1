Summary: Scripts for managing a Highly Available CVMFS Stratum1 pair of machines
Name: cvmfs-hastratum1
Version: 2.22
# The release_prefix macro is used in the OBS prjconf, don't change its name
%define release_prefix 1
Release: %{release_prefix}%{?dist}
Group: Applications/System
License: BSD
# https://github.com/cvmfs-contrib/cvmfs-hastratum1/archive/v%{version}.tar.gz
Source: cvmfs-hastratum1-%{version}.tgz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
Requires: cvmfs-server
Requires: python-anyjson

%description
%{summary}

%prep
%setup

%install
[[ %{buildroot} != / ]] && rm -rf %{buildroot}
ls
make PREFIX=%{buildroot} install

%post
# compress uncompressed logs
find /var/log/cvmfs -name '*.log-*' ! -name "*.gz" | xargs --no-run-if-empty gzip

%clean
[[ %{buildroot} != / ]] && rm -rf %{buildroot}

%files
/usr/bin/*
/usr/sbin/*
/etc/ha.d/*.in
/etc/ha.d/resource.d/*
/etc/cvmfs/*
/etc/logrotate.d/*
/usr/share/cvmfs-hastratum1/*
%dir /var/lib/cvmfs-hastratum1
%ghost /var/lib/cvmfs-hastratum1/*

%changelog
* Mon Sep 23 2019 Dave Dykstra <dwd@fnal.gov> 2.22-1
- Remve use of the ssh arcfour cipher; it doesn't work on el7.

* Mon May 13 2019 Dave Dykstra <dwd@fnal.gov> 2.21-1
- Apply addcmd and remcmd sequentially in manage-replicas, so different
  values can be used by different repositories.
- Make buildable on OpenSUSE Build System

* Mon Jun 13 2017 Dave Dykstra <dwd@fnal.gov> 2.20-1
- Change add-repository -H to also go ahead if an initial snapshot
  exists on the partner, to support the case of bootstrapping a
  completely wiped backup machine.  In that case, have it snapshot
  from the partner.
- Remove generate_replicas

* Mon May 01 2017 Dave Dykstra <dwd@fnal.gov> 2.19-1
- Use the -p option to add-replica in add-repository, to avoid creating
  the httpd configuration file.
- When an addcmd fails, do not call remcmd if the --continue-failed option
  was given.

* Thu Feb 09 2017 Dave Dykstra <dwd@fnal.gov> 2.18-1
- Change add-repository to make an updating lock while doing the rsync,
  so manage-replicas won't try to start another add-repository during
  that time.

* Thu Feb 09 2017 Dave Dykstra <dwd@fnal.gov> 2.17-1
- Change add-repository to clean up the repository storage if
  add-replica fails.  This prevents a situation of confusion between
  good old data and bad new data.

* Thu Feb 09 2017 Dave Dykstra <dwd@fnal.gov> 2.16-1
- Make sure that /usr/sbin is in the PATH inside manage-replicas-log
  and restore-replicas. The former is typically run from cron and the
  latter from puppet, and those don't necessarily have /usr/sbin in
  the path.

* Tue Feb 07 2017 Dave Dykstra <dwd@fnal.gov> 2.15-1
- Fix off by one error in manage-replicas-log
- Add manage-replicas -d option and use it in manage-replicas-log to
  pass in $STORAGE so the -c option can correctly know when an
  initial snapshot isn't completely finished
- Change manage-replicas to accept 'repositories' (from a stratum0) in
  addition to 'replicas' from a replist

* Tue Feb 07 2017 Dave Dykstra <dwd@fnal.gov> 2.14-1
- Allow add-repository to reuse old data even when not using -h
- Redirect most of restore-replicas output to a file

* Tue Feb 07 2017 Dave Dykstra <dwd@fnal.gov> 2.13-1
- Add '--continue-failed' option to manage-replicas
- Add manage-replicas-log function for handling logging of parallel
  manage-replicas processes
- Make restore-replicas a little more robust

* Tue Feb 07 2017 Dave Dykstra <dwd@fnal.gov> 2.12-1
- Add restore-replicas command for restoring the replica configurations
  on a freshly reinstalled backup machine.

* Fri Feb 06 2017 Dave Dykstra <dwd@fnal.gov> 2.11-1
- Fix bugs in manage-replicas having to do with replacing source urls
  when they change.

* Fri Feb 03 2017 Dave Dykstra <dwd@fnal.gov> 2.10-1
- Add manage-replicas command

* Tue Jan 17 2017 Dave Dykstra <dwd@fnal.gov> 2.9-1
- Copy the reflog.chksum file to the backup machine in add-repository,
  when it is invoked without -h.

* Tue Jan 17 2017 Dave Dykstra <dwd@fnal.gov> 2.8-1
- Remove .cvmfsreflog if it is present when adding repository back on
  existing data with add-repository -h.

* Tue Oct 18 2016 Dave Dykstra <dwd@fnal.gov> 2.7-1
- Back out the change from 2.6-1 and instead add script cvmfsha-gc-all
  that runs garbage collection on all repositories that have garbage
  collection enabled on the stratum 0.  Call it from cron on both
  master and backup machines, and redirect output to a log file.

* Mon Oct 17 2016 Dave Dykstra <dwd@fnal.gov> 2.6-1
- Change add-repository to always use cvmfs_server add-replica -z to enable
  garbage collection when it is available in the upstream repository.

* Tue Aug 30 2016 Dave Dykstra <dwd@fnal.gov> 2.5-1
- Add -H option to add-repository that's just like -h except will only
  add if some old data is present.
- Add -h option to remove-repository to remove only the current HA half
  and leave data behind.
- Add -t option to generate_replicas to only generate a short list of
  test replicas rather than the whole list.

* Fri May 25 2016 Dave Dykstra <dwd@fnal.gov> 2.4-1
- Compress log files

* Fri Mar 25 2016 Dave Dykstra <dwd@fnal.gov> 2.3-1
- Allow pull_and_push to take over if both sides of a repository are
  made with add-repository -h.
- Hide error message in pull_and_push ABORT command coming from second
  kill attempt if the first attempt succeeded.
- Add support for cvmfs-server-2.2.X's info directory
- Allow parallel pull_and_push commands, up to $MAXPARALLELPULL which
  defaults to 4.

* Mon Oct 19 2015 Dave Dykstra <dwd@fnal.gov> 2.2-1
- Change add-repository to allow a domain public key to be missing if
  $EXTRAKEYS is set.  This is to support repositories from any domain
  being signed by the OSG public key.
- Add -h option to add-repository to add on only current half of ha pair
  of machines.  This is for use when re-installing a machine.
- Change add-repository to ignore differences in file modification times
  of the data between the master and backup machines.
- Change pull_and_push to not do push if remote side hasn't finished
  initial snapshot, because the initial snapshot can take a long time
  when re-installing a machine from scratch including the data.
- Change pull_and_push ABORT to kill with -15 instead of -9, so that
  cvmfs_server can clean up any locks before exiting.

* Wed Apr 08 2015 Dave Dykstra <dwd@fnal.gov> 2.1-1
- If /etc/cvmfs/keys/$REPO.pub exists, use that as the key instead of a
  domain key.

* Wed Mar 25 2015 Dave Dykstra <dwd@fnal.gov> 2.0-1
- Remove Requires: heartbeat so package can also work without heartbeat
- For convenience of non-heartbeat system, add a symlink pointing to
    /etc/ha.d/resource.d/cvmfs-push-abort
  at
    /usr/share/cvmfs-hastratum1/push-abort
- Add /usr/bin/cvmfsha-is-master and cvmfsha-is-backup which return an
  exit code of 0 only on the master machine or backup machine
  respectively (it is possible to be neither).  If the hastratum1.conf
  configuration variable IS_HA_MASTER_CMD or IS_HA_BACKUP_CMD
  respectively are set, the command listed will be eval'ed to
  determine this; if the variables are not set, the corresponding
  heartbeat commands are used.
- Add "cvmfsha-" prefix symlinks for each of the /usr/sbin tools
- Add OSG support tools in /usr/share/cvmfs-hastratum1: print-osg-repos
  and generate-osg-replicas
- Add general tool /usr/bin/watch-network-q for watching queued network
  requests 

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
