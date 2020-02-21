# Python program to query aws ec2 instance metadata in json format

# Program  getMetadata.py

* Down this program and copy to  `/usr/local/bin/`
* Give execute permissions `chmod +x /usr/local/bin/getMetadata.py`
* To get help  `getMetadata.py --help`
```
Syntax: /usr/local/bin/getMetadata.py [options]

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
```

# Query a perticular data key 

```
[ec2-user@ip-XXX-31-85-XXX ~]$ getMetadata.py --ami-id
{
    "ami-id": "ami-0a887e401f7654935"
}
```
```
[ec2-user@ip-XXX-31-85-XXX ~]$ getMetadata.py --mac
{
    "mac": "unavailable"
}
```
```
[ec2-user@ip-XXX-31-85-XXX ~]$ getMetadata.py --events
{
    "events": "unavailable"
}
```

# Query multiple data keys
```
[ec2-user@ip-XXX-31-85-XXX ~]$ getMetadata.py  --hostname --local-ipv4 --network --block-device-mapping
{
    "block-device-mapping": "ami\nroot",
    "hostname": "ip-XXX-31-85-XXX.ec2.internal",
    "local-ipv4": "XXX.31.85.XXX",
    "network": "unavailable"
}

```

# Query all the keys ( if no perticular key is provided ) 

```
[ec2-user@ip-XXX-31-85-XXX ~]$  getMetadata.py
{
    "ami-id": "ami-0a887e401f7654935",
    "ami-launch-index": "0",
    "ami-manifest-path": "(unknown)",
    "block-device-mapping": "ami\nroot",
    "events": "unavailable",
    "hostname": "ip-XXX-31-85-XXX.ec2.internal",
    "identity-credentials": "unavailable",
    "instance-action": "unavailable",
    "instance-id": "i-047abcdssc0d9a1d3",
    "instance-type": "t2.micro",
    "local-hostname": "ip-XXX-31-85-XXX.ec2.internal",
    "local-ipv4": "XXX.31.85.XXX",
    "mac": "unavailable",
    "managed-ssh-keys": "unavailable",
    "metrics": "unavailable",
    "network": "unavailable",
    "placement": "availability-zone",
    "profile": "default-hvm",
    "public-hostname": "ec2-3-86-XXX-XXX.compute-1.amazonaws.com",
    "public-ipv4": "3.86.XXX.XXX",
    "public-keys": [
        "ssh-rsa AAAAB3NzaC1yc2EAAAADAQAsasaJSAdYOSnnnSAPPKDWWWWWWUAntG2MA1w7Vx8DbhvnhWhU/fVK8hU4TeLr/XnlGSbs13rm1NiS+G/faM08N9DXbocHwcZlZjgz5jPP9fXAiXtTNx/o4re5JI59G/y00r4MbFT3MTOsPO0JudLKsnqFCGnuGKtuaYDra8ww4KmqEANxrlu0EIYGvmM/AvyEMglan/ozjLZd7t2oBUmGPnnBcX/yKGkcphtWGfedxTv2hWPrcSMasWscftlPhm7t8ug4tKSSChhvwMIMTIILvlcus+W2RZiJ8ZrTSzAnWebLiY9sp4bu3fZxQly+t hello-useast1-KP"
    ],
    "reservation-id": "r-0845esS7A8seb42a54",
    "security-groups": "launch-wizard-1",
    "services": "unavailable"
}
```
