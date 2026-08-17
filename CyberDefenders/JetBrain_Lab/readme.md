# CTF Forensics Report — JetBrain Lab

## Statement
During a recent security incident, an attacker successfully exploited a vulnerability in our web server, allowing them to upload webshells and gain full control over the system. The attacker utilized the compromised web server as a launch point for further malicious activities, including data manipulation. 

As part of the investigation, You are provided with a packet capture (PCAP) of the network traffic during the attack to piece together the attack timeline and identify the methods used by the attacker. The goal is to determine the initial entry point, the attacker's tools and techniques, and the compromise's extent.

## Challenge Info
- **Name:** JetBrain Lab
- **Origin:** CyberDefenders
- **Category:** Network Forensics
- **Date:** 2026-08-16

## Tools Used
-`wireshark`

## Findings

### Question 1 — Identifying the attacker's IP address helps trace the source and stop further attacks. What is the attacker's IP address?

- Answer: `23.158.56.196`

![info of file](./screenshots/info_file.png)


### Step 2 — Identifying the type of Encoding 



### Step 3 - Decoding the File



### Step 4 - Checking the String with CyberChef .



## Flag



## Conclusion


