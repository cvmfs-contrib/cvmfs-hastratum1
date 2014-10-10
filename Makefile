PREFIX=/usr/local

all:

install:
	install -D -m 555 pull_and_push $(PREFIX)/usr/sbin/pull_and_push
	install -D -m 555 add-repository $(PREFIX)/usr/sbin/add-repository
	install -D -m 555 remove-repository $(PREFIX)/usr/sbin/remove-repository
	install -D -m 644 ha.cf.in $(PREFIX)/etc/ha.d/ha.cf.in
	install -D -m 644 haresources.in $(PREFIX)/etc/ha.d/haresources.in
	install -D -m 555 cvmfs-push-abort $(PREFIX)/etc/ha.d/resource.d/cvmfs-push-abort
	install -D -m 555 ha-takeover $(PREFIX)/etc/ha.d/resource.d/ha-takeover
	install -D -m 600 authkeys.in $(PREFIX)/etc/ha.d/authkeys.in
	install -D -m 644 hastratum1.conf.in $(PREFIX)/etc/cvmfs/hastratum1.conf.in
	install -D -m 444 hastratum1.logrotate $(PREFIX)/etc/logrotate.d/cvmfs-hastratum1
