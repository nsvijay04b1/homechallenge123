#!/usr/bin/python

"""
Query and display EC2 metadata

If no options are provided, all options will be displayed

Options:
    -h --help               show this help

    --ami-id                display the ami id
    --ami-launch-index      display the ami launch index
    --ami-manifest-path     display the ami manifest path
    --block-device-mapping  display the block device id
    --events                display events like maintenance
    --hostname              display the local hostname
    --instance-id           display the instance id
    --instance-type         display the instance type
    --identity-credentials  display identity credentials
    --instance-action       display instance action
    --local-ipv4            display the local ipv4 ip address
    --local-hostname        display the local hostname
    --mac                   MAC address of the instance
    --managed-ssh-keys      display managed ssh keys
    --metrics               display metrics
    --network               display the network interfaces usd
    --placement             display the placement of ec2 instance
    --public-keys           display the openssh public keys
    --public-hostname       display the public hostname
    --public-ipv4           display the public ipv4 ip address
    --profile               display the profile
    --reservation-id        display the reservation id
    --security-groups       display the security groups
    --services              display the services

"""

import sys
import time
import getopt
import urllib
import socket
import json

METAOPTS = ['ami-id', 'ami-launch-index', 'ami-manifest-path', 'block-device-mapping', 'events',
'hostname',  'instance-id', 'instance-type', 'local-hostname', 'instance-action',
'local-ipv4', 'mac', 'metrics', 'network', 'placement', 'profile', 'public-hostname',
'public-ipv4', 'public-keys', 'reservation-id', 'security-groups', 'services' ,'identity-credentials', 'managed-ssh-keys']

class Error(Exception):
    pass

class EC2Metadata:
    """Class for querying metadata from EC2"""

    def __init__(self, addr='169.254.169.254', api='2008-02-01'):
        self.addr = addr
        self.api = api

        if not self._test_connectivity(self.addr, 80):
            raise Error("could not establish connection to: %s" % self.addr)

    @staticmethod
    def _test_connectivity(addr, port):
        for i in range(6):
            s = socket.socket()
            try:
                s.connect((addr, port))
                s.close()
                return True
            except socket.error, e:
                time.sleep(1)

        return False

    def _get(self, uri):
        url = 'http://%s/%s/%s/' % (self.addr, self.api, uri)
        value = urllib.urlopen(url).read()
        if "404 - Not Found" in value:
            return None

        return value

    def get(self, metaopt):
        """return value of metaopt"""

        if metaopt not in METAOPTS:
            raise Error('unknown metaopt', metaopt, METAOPTS)

        if metaopt == 'availability-zone':
            return self._get('meta-data/placement/availability-zone')

        if metaopt == 'region':
            return self._get('meta-data/region')

        if metaopt == 'public-keys':
            data = self._get('meta-data/public-keys')
            keyids = [ line.split('=')[0] for line in data.splitlines() ]

            public_keys = []
            for keyid in keyids:
                uri = 'meta-data/public-keys/%d/openssh-key' % int(keyid)
                public_keys.append(self._get(uri).rstrip())

            return public_keys

        if metaopt == 'user-data':
            return self._get('user-data')

        return self._get('meta-data/' + metaopt)

def get(metaopt):
    """primitive: return value of metaopt"""

    m = EC2Metadata()
    return m.get(metaopt)

def display(metaopts, prefix=False):
    """primitive: display metaopts (list) values with optional prefix"""

    m = EC2Metadata()
    dicts = {}
    for metaopt in metaopts:
        value = m.get(metaopt)
        if not value:
            value = "unavailable"
        dicts[metaopt]=value

    if prefix:
        print json.dumps(dicts,sort_keys=True,indent=4)
    else:
        print json.dumps(dicts,sort_keys=True,indent=4)

def usage(s=None):
    """display usage and exit"""

    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    """handle cli options"""

    try:
        getopt_metaopts = METAOPTS[:]
        getopt_metaopts.append('help')
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h", getopt_metaopts)
    except getopt.GetoptError, e:
        usage(e)

    if len(opts) == 0:
        display(METAOPTS, prefix=True)
        return

    metaopts = []
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()

        metaopts.append(opt.replace('--', ''))

    display(metaopts)


if __name__ == "__main__":
   main()
