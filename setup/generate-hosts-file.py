#!/usr/bin/env python
import sys

try:
    ip = sys.argv[1]
except:
    ip = None

basic_hosts = [
    'init-p01st.push.apple.com',  # bag for OS X 10.8/iOS 6
]

localhost_hosts = [
    'push.apple.com',
    'courier.push.apple.com',
]

format_localhost_hosts = [
    ('%d-courier.push.apple.com', 250),
]


print '''
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1       localhost
255.255.255.255 broadcasthost
::1             localhost
fe80::1%lo0     localhost

'''

if ip:
    for host in basic_hosts:
        print "%s %s" % (ip, host)

    for host in localhost_hosts:
        print "%s %s" % ('127.0.0.1', host)

    for host, count in format_localhost_hosts:
        for i in xrange(0, count):
            print "%s %s" % ('127.0.0.1', host % i)
