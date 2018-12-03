proxy:
    proxytype: junos
    host: 100.123.1.0
    username: jcluser
    port: 830
    passwd: Juniper!1
local_asn: 101
neighbors:
   - interface: ge-0/0/0
     asn: 104
     peer_ip: 192.168.1.1 
     local_ip: 192.168.1.0
   - interface: ge-0/0/1
     asn: 105
     peer_ip: 192.168.1.3 
     local_ip: 192.168.1.2
   - interface: ge-0/0/2
     asn: 106
     peer_ip: 192.168.1.5 
     local_ip: 192.168.1.4
   - interface: ge-0/0/3
     asn: 107
     peer_ip: 192.168.1.7 
     local_ip: 192.168.1.6

