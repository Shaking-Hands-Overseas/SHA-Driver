# -*- coding: UTF-8 -*-
###                                         SHAKING HANDS OVERSEAS DRIVER 
###
### Function: Allows you to send data from an arduino to an API.
###
### Purpose:  This code was created for the Project Shaking Hands Overseas 
###           with the purpose of moving a hand from the other side of the ocean using a sensor glove.
###           
###
### NOTES:    1. Instructions of usage are explained in the README file. Check before usage
###
###           2. This code might contain issues. Please report if you found any, i will help you as soon as possible
###
### Author:   Joel Garcia (@Newtoniano20 / Newtoniano#1173 on discord)
###           Webpage: https://newtoniano20.github.io/
###
### GitHub:   https://github.com/Shaking-Hands-Overseas/SHA-Driver
###
### License:  MIT

version= "1.3"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Imports main code library
from src import *



print(f'{bcolors.HEADER}SHAKING HANDS OVERSEAS DRIVER{bcolors.ENDC} \n{bcolors.OKGREEN}Version {version} {bcolors.ENDC}\n{bcolors.OKCYAN}Author: @Newtoniano20 (Joel Garcia) {bcolors.ENDC}\n{bcolors.OKGREEN}Github:https://github.com/Shaking-Hands-Overseas/SHA-Driver {bcolors.ENDC}\n')


def main():

    # Importing Configuration File
    config, prefer = config_setup()

    # If Mode is not defined in config file, we ask the user
    if config["Mode"] == "" or config["Mode"] > 2 or prefer:
        config["Mode"] = ask_user()
    if config["Mode"] == 0:
        print(f"{bcolors.OKCYAN}[INFO] You have chosen Sender{bcolors.ENDC}")
    else:
        print(f"{bcolors.OKCYAN}[INFO] You have chosen Receiver{bcolors.ENDC}")

    # If Serial Port is not defined in config file, we ask the user
    if config["serial_port"] == "" or prefer:
        config["serial_port"] = ask_user_port()

    # We try connecting to the arduino with specified data
    while True:
        try:
            ard = arduino_connect(int(config["serial_port"]), config["BAUDRATE"])
            break
        except Exception:
            config["serial_port"] = ask_user_port()

    # We save the data to the config file
    config_write(config)

    # We Start the application
    if config["Mode"] == 0:
        sender_launcher(config, ard)

    elif config["Mode"] == 1:
        receiver_launcher(config, ard)


if __name__ == '__main__':
    main()
