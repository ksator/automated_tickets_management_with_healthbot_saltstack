import os
import json
import yaml
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def add_rule(file_name):
    files = {'topics': open('rules/' + file_name,'r')}
    r=requests.post(url + '/topics/', auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json'}, verify=False, files=files)
    print 'loaded healthbot rule ' + file_name

def add_playbook(file_name):
    files = {'playbooks': open('playbooks/' + file_name,'r')}
    r=requests.post(url + '/playbooks/', auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json' }, verify=False, files=files)
    print 'loaded healthbot playbook ' + file_name 

def add_device(dev):
    payload=json.dumps(dev)
    r = requests.post(url + '/device/' + dev['device-id'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
    print 'loaded healthbot configuration for the device: ' + dev['device-id']

def add_device_group(group):
    payload=json.dumps(group)
    r = requests.post(url + '/device-group/' + group['device-group-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
    print 'loaded healthbot configuration for the device group: ' + group['device-group-name']

def add_notification(notification):
    payload=json.dumps(notification)
    r = requests.post(url + '/notification/' + notification['notification-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
    print 'loaded healthbot configuration for the notification: ' + notification['notification-name']
    
def commit():
    r = requests.post(url + '/configuration', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print 'healthbot configuration commited!'

server = "100.123.35.0"
authuser = "jcluser"
authpwd = "Juniper!1"
url = 'https://'+ server + ':8080/api/v1'
headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json' }

devices = """[
    {
        "device-id": "vMX1",
        "host": "100.123.1.0",
        "open-config": {
            "port": 32768
        },
        "authentication": {
            "password": {
                "username": "jcluser",
                "password": "Juniper!1"
            }
        },
    },
    {
        "device-id": "vMX2",
        "host": "100.123.1.1",
        "open-config": {
            "port": 32768
        },
        "authentication": {
            "password": {
                "username": "jcluser",
                "password": "Juniper!1"
            }
        }
    },
    {
        "device-id": "vMX3",
        "host": "100.123.1.2",
        "open-config": {
            "port": 32768
        },
        "authentication": {
            "password": {
                "username": "jcluser",
                "password": "Juniper!1"
            }
        },
    },
    {
        "device-id": "vMX4",
        "host": "100.123.1.3",
        "open-config": {
            "port": 32768
        },
        "authentication": {
            "password": {
                "username": "jcluser",
                "password": "Juniper!1"
            }
        }
    },
    {
        "device-id": "vMX5",
        "host": "100.123.1.4",
        "open-config": {
            "port": 32768
        },
        "authentication": {
            "password": {
                "username": "jcluser",
                "password": "Juniper!1"
            }
        }
    },
    {
        "device-id": "vMX6",
        "host": "100.123.1.5",
        "open-config": {
            "port": 32768
        },
        "authentication": {
            "password": {
                "username": "jcluser",
                "password": "Juniper!1"
            }
        }
    },
    {
        "device-id": "vMX7",
        "host": "100.123.1.6",
        "open-config": {
            "port": 32768
        },
        "authentication": {
            "password": {
                "username": "jcluser",
                "password": "Juniper!1"
            }
        }
    }
]"""

device_group = """{
                "device-group-name" : "vmx",
                "description" : "vmx",
                "devices" : ["vMX1", "vMX2", "vMX3", "vMX4", "vMX5", "vMX6", "vMX7"],
                "playbooks" : ["openconfig"],
                "notification": {
                    "major": ["healthbot_to_saltstack"],
                    "minor": ["healthbot_to_saltstack"],
                    enable
                },
                "variable" : [
                {
                    "instance-id" : "openconfig-instance-1",
                    "playbook" : "openconfig",
                    "rule" : "bgp/check-bgp-state-using-openconfig",
                    "variable-value" : [
                    {
                        "name" : "neighbors",
                        "value" : "11.*"
                    }
                    ]
                }
                ]
            }"""

notification = """{
                 "notification-name": "healthbot_to_saltstack",
                 "description": "healthbot to saltstack webhook notifications", 
                 "http-post": {
                      "url": "http://100.123.35.1:5001/healthbot"
                  }
            }"""

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

print '**************** adding rules ************************'
rules_list=os.listdir('rules')
for rule in rules_list:
    add_rule(rule)

print '**************** adding playbooks ************************'
playbooks_list=os.listdir('playbooks')
for playbook in playbooks_list: 
    add_playbook(playbook)

print '**************** adding notifications ************************'
my_notification=yaml.load(notification)
add_notification(my_notification)

print '**************** adding devices ************************'
my_devices=yaml.load(devices)
for item in my_devices:
    add_device(item)

print '**************** adding device groups ************************'
my_group=yaml.load(device_group)
add_device_group(my_group)

print '**************** committing changeset **********************'
commit()
