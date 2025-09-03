#! /usr/bin/env python3

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
from ANSI import *

                ####################
################# Global variables #################
                ####################

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                ####################
#################    Functions     #################
                ####################

def info(text):
    print(f"{BG.GREEN}{UTIL.BOLD}[INFO]{UTIL.RESET} {timestamp} - {text}") # green bg

def warning(text):
    print(f"{BG.YELLOW}{UTIL.BOLD}[WARNING]{UTIL.RESET} {timestamp} - {text}") # yellow bg

def fail(text):
    print(f"{BG.RED}{UTIL.BOLD}[FAIL]{UTIL.RESET} {timestamp} - {text}") # red bg