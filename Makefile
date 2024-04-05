PREFIX=/usr/local

all:

install:
	install -D -m 555 pull_and_push $(PREFIX)/usr/sbin/pull_and_push
	ln -s pull_and_push $(PREFIX)/usr/sbin/cvmfsha-pull-and-push
	install -D -m 555 add-repository $(PREFIX)/usr/sbin/add-repository
	ln -s add-repository $(PREFIX)/usr/sbin/cvmfsha-add-repository
	install -D -m 555 remove-repository $(PREFIX)/usr/sbin/remove-repository
	ln -s remove-repository $(PREFIX)/usr/sbin/cvmfsha-remove-repository
	install -D -m 555 cvmfsha-gc-all $(PREFIX)/usr/sbin/cvmfsha-gc-all
	install -D -m 555 cvmfsha-is-master $(PREFIX)/usr/bin/cvmfsha-is-master
	install -D -m 555 cvmfsha-is-backup $(PREFIX)/usr/bin/cvmfsha-is-backup
	install -D -m 555 watchq $(PREFIX)/usr/bin/watch-network-q
	install -D -m 555 manage-replicas-log $(PREFIX)/usr/share/cvmfs-hastratum1/manage-replicas-log
	install -D -m 555 restore-replicas $(PREFIX)/usr/share/cvmfs-hastratum1/restore-replicas
	install -D -m 644 restore-replicas.conf.in $(PREFIX)/usr/share/cvmfs-hastratum1/restore-replicas.conf.in
	install -D -m 555 print_osg_repos $(PREFIX)/usr/share/cvmfs-hastratum1/print-osg-repos
	install -D -m 644 ha.cf.in $(PREFIX)/etc/ha.d/ha.cf.in
	install -D -m 644 haresources.in $(PREFIX)/etc/ha.d/haresources.in
	install -D -m 555 cvmfs-push-abort $(PREFIX)/etc/ha.d/resource.d/cvmfs-push-abort
	ln -s ../../../etc/ha.d/resource.d/cvmfs-push-abort $(PREFIX)/usr/share/cvmfs-hastratum1/push-abort
	install -D -m 555 ha-takeover $(PREFIX)/etc/ha.d/resource.d/ha-takeover
	install -D -m 600 authkeys.in $(PREFIX)/etc/ha.d/authkeys.in
	install -D -m 644 hastratum1.conf.in $(PREFIX)/etc/cvmfs/hastratum1.conf.in
	install -D -m 444 hastratum1.logrotate $(PREFIX)/etc/logrotate.d/cvmfs-hastratum1
	# ghost files
	install -D -m 644 /dev/null $(PREFIX)/var/lib/cvmfs-hastratum1/restoration-date
	install -D -m 644 /dev/null $(PREFIX)/var/lib/cvmfs-hastratum1/restore-replicas.conf
	install -D -m 644 /dev/null $(PREFIX)/var/lib/cvmfs-hastratum1/restore-replicas.out
