# CTF Forensics Report — Hidden in plainsight

## Statement
You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.

## Challenge Info
- **Name:** Hidden in plainsight
- **Origin:** pico-ctf 
- **Category:** Forensics
- **Date:** 2026-03-21

## Tools Used
-`exiftool`, `CyberChef`

## Findings

### Step 1 — Image JPG Analysis with exiftool
- Command: `exiftool img.jpg`

![info of image file](./screenshots/exiftool.png)

- Result: The Comment field contained an unusual Base64-encoded string: c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9

### Step 2 — Analysis of the Comment string with CyberChef 

![result](./screenshots/comments%20base64.png)

- Result: Pasted the Comment value into CyberChef and applied From Base64, which decoded the following phrase.

    `steghide:cEF6endvcmQ=`

### Step 3 - Decoding the phrase again with CyberChef

![info of phrase](./screenshots/result%20of%20comments.png)

- Result: After decoding "cEF6endvcmQ=" we obtain "pAzzword" and with this password we can decode the metadata with steghide.


### Step 4 - Extracting the Hidden File with steghide

 `Command: steghide extract -sf img.jpg` 

![info](./screenshots/extracting%20data.png)

- Result : After running the command and entering pAzzword as the passphrase, steghide extracted flag.txt, which contained the flag.txt


## Flag

`picoCTF{h1dd3n_1n_1m4g3_e7f5b969}`

## Conclusion

This challenge demonstrated a layered encoding technique: a Base64 string was embedded in the JPG's EXIF Comment field, which itself decoded to another Base64-encoded steghide passphrase. Using that passphrase with steghide extract revealed the hidden flag.txt containing the flag.