# About this project

# Documentation structure

# About the lab

## Building blocks 
- Some Junos devices 
- One Ubuntu VM (16.04) for healthbot (1.0)
- One Ubuntu VM (16.04) for SaltStack and Request Tracker

## IP addresses 
Here are the management ip addresses I am using in my scripts.  
Update the scripts to use the management ip addresses of your lab.  
You can use less Junos devices if you want (you need at least 2 devices to test protocols).    

| Host        | Management IP address           |
| ------------- |:-------------:| 
| ubuntu        | 100.123.35.0 |
| ubuntu1        | 100.123.35.1 |
| vMX1      | 100.123.1.0 |
| vMX2      | 100.123.1.1   |
| vMX3      | 100.123.1.2   |
| vMX4      | 100.123.1.3   |
| vMX5      | 100.123.1.4   |
| vMX6      | 100.123.1.5   |
| vMX7      | 100.123.1.6   |

## Ubuntu details

```
$ lsb_release -a
```

## Junos details

### Junos version
```
lab@dc-vmx-3> show version | match telemetry
```
```
lab@dc-vmx-3> show version | match openconfig
```

### Junos configuration
```
lab@dc-vmx-3> show configuration system services extension-service | display set
```
```
lab@dc-vmx-3> show configuration system services netconf | display set
```

## other componants

The other componants (docker, SaltStack, python libraries, heathbot ...) will be installed using the below instructions.

# instructions

clone this repository 
```
$ git clone
$ cd 
```

## instructions about the host ```ubuntu```

### install heathbot
This is not covered

### configure healthbot 

## instructions about the hosthost ```ubuntu1``` 

### Install Docker on the ubuntu host ```ubuntu1```

Check if Docker is already installed on the ubuntu host ```ubuntu1```
```
$ docker --version
```

If it was not already installed, install it:
```
$ sudo apt-get update
```
```
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```
```
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
```
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```
```
$ sudo apt-get update
```
```
$ sudo apt-get install docker-ce
```
```
$ sudo docker run hello-world
```
```
$ sudo groupadd docker
```
```
$ sudo usermod -aG docker $USER
```

Exit the ssh session to ```ubuntu1``` and open an new ssh session to ```ubuntu1``` and run these commands to verify you installed Docker properly:  
```
$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```
```
$ docker --version
Docker version 18.03.1-ce, build 9ee9f40
```

### Request Tracker

Request Tracker (RT) is an open source issue tracking system.  
There is a Request Tracker Docker image available https://hub.docker.com/r/netsandbox/request-tracker/  

#### Pull a Request Tracker Docker image on the ubuntu host ```ubuntu1```

Check if you already have it locally:   
```
$ docker images
```

if not, pull the image:
```
$ docker pull netsandbox/request-tracker
```
Verify: 
```
$ docker images
REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
netsandbox/request-tracker   latest              b3843a7d4744        4 months ago        423MB
```

#### Instanciate a Request Tracker container on the ubuntu host ```ubuntu1```
```
$ docker run -d --rm --name rt -p 9081:80 netsandbox/request-tracker
```
Verify: 
```
$ docker ps
CONTAINER ID        IMAGE                        COMMAND                  CREATED             STATUS                  PORTS                                                 NAMES
0945209bfe14        netsandbox/request-tracker   "/usr/sbin/apache2 -…"   26 hours ago        Up 26 hours             0.0.0.0:9081->80/tcp                                  rt
```

### Verify you can access to RT GUI

Access RT GUI with ```http://100.123.35.1:9081``` in a browser.  
The default ```root``` user password is ```password```

### Install the ```rt``` python library on the ubuntu host ```master1```

There are python libraries that provide an easy programming interface for dealing with RT:  
- [rtapi](https://github.com/Rickerd0613/rtapi) 
- [python-rtkit](https://github.com/z4r/python-rtkit)
- [rt](https://github.com/CZ-NIC/python-rt) 

Install the ```rt``` library on the ubuntu host ```master1```

```
$ sudo -s
```
```
# apt-get install python-pip
```
```
# pip install requests nose six rt
```
Verify
```
# pip list
```

### Verify you can use ```rt``` Python library on the ubuntu host ```master1```
Python interactive session on the ubuntu host ```master1```: 
```
# python
Python 2.7.12 (default, Dec  4 2017, 14:50:18)
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import rt
>>> tracker = rt.Rt('http://100.123.35.1:9081/REST/1.0/', 'root', 'password')
>>> tracker.url
'http://100.123.35.1:9081/REST/1.0/'
>>> tracker.login()
True
>>> tracker.search(Queue='General', Status='new')
[]
>>> tracker.create_ticket(Queue='General', Subject='abc', Text='bla bla bla')
1
>>> tracker.reply(1, text='notes you want to add to the ticket 1')
True
>>> tracker.search(Queue='General')
[{u'Status': u'open', u'Priority': u'3', u'Resolved': u'Not set', u'TimeLeft': u'0', u'Creator': u'root', u'Started': u'Wed Jul 11 09:30:57 2018', u'Starts': u'Not set', u'Created': u'Wed Jul 11 09:30:10 2018', u'Due': u'Not set', u'LastUpdated': u'Wed Jul 11 09:30:57 2018', u'FinalPriority': u'0', u'Queue': u'General', 'Requestors': [u''], u'Owner': u'Nobody', u'Told': u'Not set', u'TimeEstimated': u'0', u'InitialPriority': u'0', u'id': u'ticket/1', u'TimeWorked': u'0', u'Subject': u'abc'}]
>>> for item in  tracker.search(Queue='General'):
...    print item['id']
...
ticket/1
>>> tracker.logout()
True
>>> exit()
```

### Using RT GUI, verify the ticket details you created previously with Python interactive session
