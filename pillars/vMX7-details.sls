proxy:
    proxytype: junos
    host: 100.123.1.6
    username: jcluser
    port: 830
    passwd: Juniper!1
local_asn: 107
neighbors:
   - interface: ge-0/0/0
     asn: 101
     peer_ip: 192.168.1.6 
     local_ip: 192.168.1.7
   - interface: ge-0/0/1
     asn: 102
     peer_ip: 192.168.2.6 
     local_ip: 192.168.2.7
   - interface: ge-0/0/2
     asn: 103
     peer_ip: 192.168.3.6 
     local_ip: 192.168.3.7


