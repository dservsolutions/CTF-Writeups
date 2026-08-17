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

- Result: After applied these commands, we can see that this is a string file with a lot of characters. Let's 
dig what;s inside with the command below.

- Command: `head -10 logs.txt`

![head command](./screenshots/head_command.png)

![head result](./screenshots/head_logsfile.png)

- Result: We can see it's a plain text file containing a large block of characters.

### Step 2 — Identifying the type of Encoding 

Let's identify the file using two methods Hex(only) or Base64.

- Hex only 0-9, a-f

- Command: `head -1 logs.txt | grep -P '^[0-9a-fA-F]+$'`

- Result: None

- Base64 characters are A-Z, a-z, 0-9, +, /, ends with = or ==

- Command: `head -1 logs.txt | grep -P '^[A-Za-z0-9+/=]+$' `

- Result:

![result](./screenshots/base64result.png)

- Conclusion: Base64 Encoded File.

### Step 3 - Decoding the File

After identifying the encoding type, we proceed to decode the file.

- Command: `base64 -d logs.txt > decode`

![decoding ](./screenshots/decoding_file_command.png)

- Result : File called decode, let's check the type of file with the command below.

- Command: `file decode`

![type of file](./screenshots/type_of_file.png)

- Result: After checking the file type, we noticed the file is PNG image file.

![file](./screenshots/img.png)

- Result: At the bottom of the image we can see a long chain of string. let's check out at
step four.

### Step 4 - Checking the String with CyberChef .

- We need to use the CyberChef's Magic recipe in order to get the type.

![info](./screenshots/magic_mode.png)

- Result : After use the Magic recipe we identified the encoding as hexadecimal.

## Flag

`picoCTF{forensics_analysis_is_amazing_ec1984fc7}`

## Conclusion

This challenge demonstrates that data can be hidden inside another file type, and that hidden messages can themselves be encoded. It's a good reminder to be careful about the files we download to our machines, and to always inspect files beyond their surface appearance.
