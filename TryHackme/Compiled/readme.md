# CTF Purple Team Report — Compiled

## Hint

Strings can only help you so far.


## Statement

Download the task file and get started. The binary can also be found in the AttackBox inside the /root/Rooms/Compiled/ directory.

Note: The binary will not execute if using the AttackBox. However, you can still solve the challenge.



## Challenge Info
- **Name:** Compiled
- **Origin:** Tryhackme 
- **Category:** Purple Team
- **Date:** 2026-04-01

## Tools Used
-`file`, `strings`, `GHidra`

## Findings

### Step 1 — Analysis of the filename with `file` command

- After downloaded the filename `Compiled-1688545393558.Compiled`

    ![file](./screenshots/file_downloaded.png)

- We proceed to analize the file with the linux command `file`

- Command: `file Compiled-1688545393558.Compiled`  

- Result: 

    ![file_analisys](./screenshots/file_command.png)


### Step 2 — Strings analisys of the file

- After confirm the framework of the webpage we crafted a basic syntax to confirm the SSTI.

- Command: `{{7*7}}`


    ![result](./screenshots/input.png)

- Result: After applying the command, the result was:


    ![result_input](./screenshots/result1.png)

- Result: After the result obtained we can confirm that the site is vulnerable to SSTI via Jinja2


### Step 3 — Ghidra analisys of the file 

- Command: `{{"".__class__.__mro__[1].__subclasses__()}}`

    ![payload](./screenshots/payload_command.png)

- Breakdown of the command: `"".__class__.__mro__[1]` Accesses the base object class, the superclass of all Python classes.

- Breakdown of the command: `__subclasses__()` List all subclasses object and [356] the index for the `subprocess.Popen` class (this index may vary and should be checked in the target environment)

    ![payload_result](./screenshots/payload_result.png)

### Step 4 — Password Obtained.


## Flag

`DoYouEven_init`

## Conclusion


    

