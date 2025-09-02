#!/usr/bin/env python3

                ####################
#################   Informations   #################
                ####################

Version     = "1.1.0"
Credits     = "spaghetata"
License     = "GPL3.0"
Discription = "This is a small script for error handling"

                ####################
#################      Import      #################
                ####################

from datetime import datetime

                ####################
################# Global variables #################
                ####################

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                ####################
#################    Functions     #################
                ####################

def info(text):
    print(f"\033[48;5;34m[INFO]\033[0m {timestamp} - {text}") # green bg

def warning(text):
    print(f"\033[43m[WARNING]\033[0m {timestamp} - {text}") # yellow bg

def fail(text):
    print(f"\033[41m[FAIL]\033[0m {timestamp} - {text}") # red bg