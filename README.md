# About this project

Event driven automation using Healthbot and SaltStack and Junos

- Healthbot is used to collect data from the network, store the data collected, process the data collected.  
- Based on healthbot configuration and network devices status, webhook notifications are sent from healthbot to SaltStack.  
- SaltStack reacts to these notifications.  
    - SaltStack automatically creates a new RT (Request Tracker) ticket to track the issue. If there is already an
existing ticket to track this issue, SaltStack updates the existing ticket instead of creating a new one. 
    - The relevant content of the webhook notifications from Healthbot is automatically added to the appropriate tickets.
    - SaltStack automatically collects "show commands" from the faulty junos device and attach the device output to the appropriate tickets.
    
Here's a video with a demo https://www.youtube.com/watch?v=XJ-5SK3P3gI&index=7&list=PLGvolzhkU_gSClZHCzzDQ0_6vROrt5Gpu&t=0s 

# Instructions

clone the repository and visit the [repository wiki pages](https://github.com/ksator/automated_tickets_management_with_healthbot_saltstack/wiki)
