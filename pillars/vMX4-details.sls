proxy:
    proxytype: junos
    host: 100.123.1.3
    username: jcluser
    port: 830
    passwd: Juniper!1
local_asn: 104
neighbors:
   - interface: ge-0/0/0
     asn: 101
     peer_ip: 192.168.1.0 
     local_ip: 192.168.1.1
   - interface: ge-0/0/1
     asn: 102
     peer_ip: 192.168.2.0 
     local_ip: 192.168.2.1
   - interface: ge-0/0/2
     asn: 103
     peer_ip: 192.168.3.0 
     local_ip: 192.168.3.1

