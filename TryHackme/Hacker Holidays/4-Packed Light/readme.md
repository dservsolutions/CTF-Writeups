# Hacker Holidays — Packet Light

## Hint

Analyze the provided capture for a covert communication channel.
 
Identify where the exfiltrated data is being hidden and reassemble it.
 
Decode the recovered data and submit the flag.

## Statement

Tiny packets. Odd hours. Suspiciously regular. Someone's smuggling out the data equivalent of a hotel towel every night, folded neatly inside traffic that looks ordinary until you decode it.

A short capture from the guest network is all VERA could pull before the connection dropped. Somewhere in that traffic, a quiet little errand is running on a loop, and it isn't part of any service the hotel actually offers.



## Challenge Info
- **Name:** Packet Light
- **Origin:** Tryhackme 
- **Category:** Red Team
- **Date:** 07-30-2026

## Tools Used
-`gobuster`, `gitdump`, `texteditor`

## Findings

### Step 1 — Analisys of the Lab Machine.

- After the lab machine loaded and opened the address provided `http://10.144.176.255:8080`

    ![file](./screenshots/web_page.png)

- I've observe non secure webpage. 

    ![file_analisys](./screenshots/http.png)


### Step 2 — Enumerating the directory to find exposed endpoints.

- Applying the following command to inspect the website.

- Command: `gobuster dir -u http://10.146.174.187:8080/ -w /root/Desktop/Tools/wordlists/SecLists/Discovery/Web-Content/common.txt` part of the result I'll show bellow.

    ![strings_result](./screenshots/gobuster_result.png)


### Step 3 — Analysing the endpoint founded. 

- After checking the endpoint exposed means that the whole .git object database is likely reached too.
    This is our entry point.

- Verifying it's a readable directory with the following curl command:

    `curl http://10.144.176.255:8080/.git/HEAD` 

- After applying the command we get the following result: 

    `ref: refs/heads/main` Meaning that the objects, refs, and logs are almost certainly fetchable too.

![repo](./screenshots/gitrepo.png)


### Step 4 — Dumping the full repo with `git-dumper`.

- Installing the python script:  `pip install git-dumper --break-system-packages`

- Applying the command to dumpt the repo: 

    `git-dumper http://10.144.176.255:8080/.git ./byte-lotus-src`

    ![dump](./screenshots/git_dump_command.png)

- After dumping the repo we found the app 

    ![app](./screenshots/app_downloaded.png)

- Inspecting the Readme file: 

    ![readme_file](./screenshots/flag.png)

### Flag `THM{byt3_l0tus_n3v3r_f0rg3ts}`


    

