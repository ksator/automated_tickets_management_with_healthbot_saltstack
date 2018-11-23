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
        "variable" : [
        {
            "instance-id" : "enforce-int-state-instance-1",
            "playbook" : "enforce-int-state",
            "rule" : "interfaces/enforce-interfaces-state",
            "variable-value" : [
            {
                "name" : "interface_name",
                "value" : "ge-0/0/0"
            }
            ]
        }
        ]
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
        "variable" : [
        {
            "instance-id" : "enforce-int-state-instance-1",
            "playbook" : "enforce-int-state",
            "rule" : "interfaces/enforce-interfaces-state",
            "variable-value" : [
            {
                "name" : "interface_name",
                "value" : "ge-*|xe-*"
            }
            ]
        }
        ]
    }
]"""

# update this section with your device group details
device_group = """{
                "device-group-name" : "vmx",
                "description" : "vmx",
                "devices" : ["vMX1", "vMX2", "vMX3", "vMX4", "vMX5", "vMX6", "vMX7"],
                "playbooks" : ["enforce-int-state"],
                "variable" : [
                {
                    "instance-id" : "enforce-int-state-instance-1",
                    "playbook" : "enforce-int-state",
                    "rule" : "interfaces/enforce-interfaces-state"
                }
                ]
            }"""

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

print '**************** adding rules ************************'
rules_list=os.listdir('rules')
for rule in rules_list:
    add_rule('enforce-interfaces-state.rule')

print '**************** adding playbooks ************************'
playbooks_list=os.listdir('playbooks')
for playbook in playbooks_list: 
    add_playbook('enforce-int-state.playbook')

print '**************** adding devices ************************'
my_devices=yaml.load(devices)
for item in my_devices:
    add_device(item)

print '**************** adding device groups ************************'
my_group=yaml.load(device_group)
add_device_group(my_group)

print '**************** committing changeset **********************'
commit()
