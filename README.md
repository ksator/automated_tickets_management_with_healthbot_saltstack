# About this project

Event driven automation using Healthbot and SaltStack 

- Healthbot is used to collect data from the network, store the data collected, process the data collected.  
- Based on healthbot configuration and network devices status, webhook notifications are sent from healthbot to SaltStack.  
- SaltStack reacts to these notifications.  
    - SaltStack automatically creates a new RT (Request Tracker) ticket to track the issue. If there is already an existing ticket to track
    this issue, SaltStack updates the existing ticket instead of creating a new one. 
    - The content of the webhook notifications from Healthbot are added to the appropriate tickets.
    - SaltStack automatically collects "show commands" output from junos devices and attach the devices output to the appropriate tickets.


# instructions

clone this repository and visit the repository wiki 
