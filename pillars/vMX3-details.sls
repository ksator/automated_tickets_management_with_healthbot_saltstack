proxy:
    proxytype: junos
    host: 100.123.1.2
    username: jcluser
    port: 830
    passwd: Juniper!1
local_asn: 103
neighbors:
   - interface: ge-0/0/0
     asn: 104
     peer_ip: 192.168.3.1 
     local_ip: 192.168.3.0
   - interface: ge-0/0/1
     asn: 105
     peer_ip: 192.168.3.3 
     local_ip: 192.168.3.2
   - interface: ge-0/0/2
     asn: 106
     peer_ip: 192.168.3.5 
     local_ip: 192.168.3.4
   - interface: ge-0/0/3
     asn: 107
     peer_ip: 192.168.3.7 
     local_ip: 192.168.3.6

