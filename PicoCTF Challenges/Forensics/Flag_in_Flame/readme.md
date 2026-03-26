# CTF Forensics Report — Flag in Flame

## Statement
The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log.
Download the encoded data here: Logs Data. Be prepared—the file is large, and examining it thoroughly is crucial .

## Challenge Info
- **Name:** Flag in flame
- **Origin:** pico-ctf 
- **Category:** Forensics
- **Date:** 2026-03-25

## Tools Used
-`file`,`wc`,`head`,`base64`,`CyberChef`

## Findings

### Step 1 — Start by understanding what's we are dealing with.

- Command: `file logs.txt` and `wc logs.txt`

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
