# ANTIBODY Launcher
# Main CLI
# Linux version
# Coded with <3 by TheMemeSniper

import colorama
import os
import requests
from io import BytesIO
import zipfile
import ftplib
import getpass

### FUNCTIONS START ###
def scriptlaunch():
    if os.path.exists("user/scripts"):
        dirlist = os.listdir("user/scripts")
        for item in dirlist:
            print(item)
        print("Type a script name to launch it")
        file = input('ABL/SCL> ')
        if os.path.exists(f"user/scripts/{file}"):
            exec(open(f"user/scripts/{file}").read())
        else:
            print(colorama.Fore.RED + f"user/scripts/{file} does not exist")
    else:
        print(colorama.Fore.RED + "user/scripts does not exist")

def downloader():
    print("Program downloader //")
    print("Provide a link to a ZIP file to automatically download, extract, and add to your scripts directory.")
    dlurl = input("ABL/DL>")
    resp = requests.get(dlurl)
    rz = requests.get(dlurl)
    print(f"{colorama.Fore.LIGHTCYAN_EX}Opened connection with {dlurl}")
    print(f"{colorama.Fore.LIGHTCYAN_EX}Downloaded ZIP contents from {dlurl}")
    with zipfile.ZipFile(BytesIO(rz.content)) as z:
        z.extractall("user/scripts")
        print(f"{colorama.Fore.LIGHTCYAN_EX}Extracted ZIP file from {dlurl} to user/scripts")
    print(colorama.Fore.LIGHTGREEN_EX + "DONE.")

def uploader():
    print("File uploader //")
    print("Provide a remote FTP server address to upload files")
    address = input("ABL/FTP/ADDRESS> ")
    username = input(f"ABL/FTP/{address}/USERNAME> ")
    password = getpass.getpass(f"ABL/FTP/{address}/{username}/PASSWORD> ")
    session = ftplib.FTP(address,username,password)
    print(f"{colorama.Fore.LIGHTGREEN_EX}Connected to {address}")
    chosenfile = input(f"{colorama.Fore.WHITE}ABL/FTP/{address}/{username}/UPLOAD> ")
    file = open(chosenfile,'rb')
    print("Sending file... ")
    session.storbinary(chosenfile, file)
    print(f"{colorama.Fore.LIGHTGREEN_EX}Successfully sent {chosenfile} to {address}")
    file.close()   
    session.quit()

def persistence():
    print("ABL Persistence //")
    print(colorama.Fore.RED + "This isn't done yet. Check back later.")
    

def utils():
    print(colorama.Fore.CYAN + '1: Forkbomb')
    print(colorama.Fore.LIGHTBLACK_EX + '2: Brick system')
    chop = input("ABL/UTILS> ")
    if chop == "1":
        print("Forkbomb launched :)")
        os.system(":(){ :|:& };:")
    elif chop == "2":
        os.system("sudo apt install vim -y")
        os.system("vim")

def prefs():
    print("ABL Options //")
    print(colorama.Fore.RED + "This isn't done yet. Check back later.")


### FUNCTIONS END ###

if os.path.exists("assets/logo.ans"):
    with open("assets/logo.ans") as logof:
        print(logof.read())
else:
    print(colorama.Fore.RED + "assets/logo.ans does not exist")

print(colorama.Fore.CYAN + 'ANTIBODY LAUNCHER')
print(colorama.Fore.LIGHTBLACK_EX + 'A script launcher optimized for tomfoolery ;)')
print(colorama.Fore.LIGHTBLACK_EX + 'Linux CLI - v1.0.0')
print(colorama.Fore.WHITE + 'Exit ABL using CTRL+C or by typing "quit"')
print("")
print(colorama.Fore.CYAN + '1: Launch a Python script')
print(colorama.Fore.LIGHTBLACK_EX + '2: Download programs')
print(colorama.Fore.CYAN + '3: Upload data')
print(colorama.Fore.LIGHTBLACK_EX + '4: Persistence')
print(colorama.Fore.CYAN + '5: Utilities')
print(colorama.Fore.LIGHTBLACK_EX + '6: ABL options')

while True:
    ci = input(colorama.Fore.WHITE + "ABL> ")
    if ci == "1":
        scriptlaunch()
    elif ci == "2":
        downloader()
    elif ci == "3":
        uploader()
    elif ci == "4":
        persistence()
    elif ci == "5":
        utils()
    elif ci == "6":
        prefs()
    elif ci == "quit":
        print(colorama.Fore.RED + "Quitting ANTIBODY Launcher...")
        exit()
    else:
        print(colorama.Fore.RED + "That option does not exist.")
        print("")
        print("Available options:")
        print(colorama.Fore.CYAN + '1: Launch a Python script')
        print(colorama.Fore.LIGHTBLACK_EX + '2: Download programs')
        print(colorama.Fore.CYAN + '3: Upload data')
        print(colorama.Fore.LIGHTBLACK_EX + '4: Persistence')
        print(colorama.Fore.CYAN + '5: Utilities')
        print(colorama.Fore.LIGHTBLACK_EX + '6: ABL options')
