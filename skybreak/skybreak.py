#!/usr/bin/python3

import os, core, time

def menu():
    core.clear()
    time.sleep(0.2)
    print(core.green + "Initializing...")
    time.sleep(0.2)
    print(core.green + "SkyBREAK ver. 1.5.89")
    print(core.green + "Interf. type " + adapter + "/" + monadapter)
    time.sleep(0.2)
    print(core.green + """\n    Welcome to skyBREAK. You have the following crackers installed:
        > WEP
        > WPA
        > WPA2""")
    try:
        ALLanswer()
    except KeyboardInterrupt:
        core.clear()
        exit()

def ALLanswer():
    answer = input("skyBREAK > ")
    if answer == "wep":
        WEPanswers()
    if answer == "wpa":
        WPAanswers("WPA")
    if answer == "wpa2":
        WPAanswers("WPA2")
    if answer == "help":
        print(core.green + """Select which crack you would like to usse by typing one of the following commands:
    > WEP
    > WPA
    > WPA2
Optionally, you can see which crackers you have installed by typing:
    > LIST""")
        ALLanswer()
    elif answer == "list":
        print(core.green + """    > WEP
    > WPA
    > WPA2""")
        ALLanswer()
    else:
        print(answer + " is not a recognized command. Type HELP for more information.")
        ALLanswer()


def WEPanswers():
    try:
        while True:
            answer = input("skyBREAK > WEP > ")
            fullanswer = answer
            answer = answer.split(" ")
            if answer[0] == "help":
                core.help("WEP")
            elif answer[0] == "ls":
                try:
                    LOCATION = answer[1]
                    os.system("ls " + LOCATION)
                except:
                    print(core.green + "Please do 'ls <LOCATION>'.")
            elif answer[0] == "scan":
                os.system('sudo airodump-ng ' + monadapter + " --encrypt WEP")
            elif answer[0] == "probe":
                try:
                    BSSID = answer[1]
                    CH = answer[2]
                    os.system("besside-ng -b" + BSSID + " -c " + CH + " " + monadapter)
                except:
                    print(core.green + "Please do 'probe <BSSID> <CH>'.")
            elif answer[0] == "crack":
                try:
                    LOCATION = answer[1]
                    os.system("aircrack-ng " + "./" + LOCATION)
                except:
                    print(core.green + "Please do 'crack <LOCATION>'.")
            elif answer[0] == "exit":
                ALLanswer()
            else:
                print(fullanswer + " is not a recognized command. Type HELP for more information.")
    except KeyboardInterrupt:
        print(core.green + "")
        ALLanswer()

def WPAanswers(sec):
    try:
        while True:
            answer = input("skyBREAK > " + sec + " > ")
            fullanswer = answer
            answer = answer.split(" ")
            if answer[0] == "help":
                core.help("WPA")
            elif answer[0] == "ls":
                try:
                    LOCATION = answer[1]
                    os.system("ls " + LOCATION)
                except:
                    print(core.green + "Please do 'ls <LOCATION>'.")
            elif answer[0] == "scan":
                os.system('sudo airodump-ng ' + monadapter)
            elif answer[0] == "capture":
                try:
                    BSSID = answer[1]
                    CH = answer[2]
                    os.system("airodump-ng -c " + CH + " --bssid " + BSSID + " -w . " + monadapter)
                except:
                    print(core.green + "Please do 'capture <BSSID> <CH>'.")
            elif answer[0] == "crack":
                try:
                    BSSID = answer[1]
                    PASSWORDLIST = answer[2]
                    LOCATION = answer[3]
                    os.system("aircrack-ng -a2 -b " + BSSID + " -w " + PASSWORDLIST + " " + LOCATION)
                except:
                    print(core.green + "Please do 'crack <BSSID> <PASSWORDLIST> <LOCATION>'.")
            elif answer[0] == "exit":
                ALLanswer()
            else:
                print(fullanswer + " is not a recognized command. Type HELP for more information.")
    except KeyboardInterrupt:
        print(core.green + "")
        ALLanswer()

core.clear()
adapter = input("Please type your WiFi Adapter/Network Interface: ")
monadapter = input("Please type your WiFi Adapter/Network Interface In Monitor Mode: ")
os.system("sudo airmon-ng start " + adapter)
menu()
