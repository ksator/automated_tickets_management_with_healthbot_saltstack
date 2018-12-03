proxy:
    proxytype: junos
    host: 100.123.1.5
    username: jcluser
    port: 830
    passwd: Juniper!1
local_asn: 106
neighbors:
   - interface: ge-0/0/0
     asn: 101
     peer_ip: 192.168.1.4 
     local_ip: 192.168.1.5
   - interface: ge-0/0/1
     asn: 102
     peer_ip: 192.168.2.4 
     local_ip: 192.168.2.5
   - interface: ge-0/0/2
     asn: 103
     peer_ip: 192.168.3.4 
     local_ip: 192.168.3.5

