# Py-logger, The python key logger

<div align="center"style="font-size:30px;">

![keyloggerImg](/Assets/KeyloggerImg.png "keyloggerImg")

</div>

---

# What is a keylogger?

When trying to exploit poor OPSEC or Social Engineer someone, keyloggers are powerfull reconnaissance tools. Used to keep a history of keys the user pressed, this can be useful for gathering information, iterperting paterns, credintials, and search histroy from the user. 

Key loggers work in a three stage process:
- Deployment
- Info Gathering
- Extraction
---
## Deployment
The deployment of a keylogger can be as simple as downloading a .exe file and running it, what varries is the method of infection. 

Key loggers can be malicously downloaded to your computer downloads via:

- Fake downloads.
- On site infection (threat actor downloads it in person).
- Hidden payloads (viruses hidden in images/ videos).

Things to consider about the deployment phase:

- A proper keylogger shouldn't be flagged by anti virus or windows firewall.
- The key logger shouldn't be detectable when active.
- The key logger shouldn't expose its method of depolyment (how it was downloaded/ prevent others from preventing the deployment).
---
## Info Gathering

While active, the key logger should keep a history of all keys pressed, mouse buttons presed (with location) and formulate words/ passwords even if the user mispells or deletes characters.

While info gathering, the key logger shouldn't hinder the users expreince as to avoid detection aswell as interfeir with important functions on the OS.

---
## Extraction

Lastly the key logger should be able to exfiltrate the key logs, exfiltration can be done in two ways:

- Logs are hidden deep in folders, where only the threat actor knows/ can figure out its location. 
- Logs are sent over the internet to a reciving computer.

When the key logger is done its functions, it should remove itself from the computer to avoid future detection, aswell as remove the logs it kept.

---
# How to use Pylogger
- run payload.py on target computer.
    - payload.py will recreate pylogger.py to avoid detection from windows defender.
- parse the produced text file keylogs.txt with pyparse.py.
    - pyparse.py will try to construct words the user typed by printing and deleting letters respecitve to the users actions.
---

# FAQ
- Py-logger is a keylogger made with python.
- Made durring hack the hill's 2023 hackathon.
- Three person dev team.
- Py-logger was primarally made for windows OS.
---
###### Hack The Hill Team: Freddy Andrews, Jacob Chiu, Emmanuel Mphande.