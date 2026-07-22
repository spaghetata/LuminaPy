#! /usr/bin/env python3

                ####################
#################   Informations   #################
                ####################

Version     = "1.3.1"
Credits     = "spaghetata"
License     = "GPL3.0"
Discription = "This is a small script for error handling"

                ####################
#################      Import      #################
                ####################

from datetime import datetime

try:
    from ANSI import *
except:
    print("ERROR: Missing Library: ANSI")
    exit(1)

                ####################
################# Global variables #################
                ####################

                ####################
#################    Functions     #################
                ####################

def info(text):
    print(f"\n{BG.GREEN}{UTIL.BOLD}[INFO]{UTIL.RESET} {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {text}") # green bg

def warn(text):
    print(f"\n{BG.YELLOW}{UTIL.BOLD}[WARN]{UTIL.RESET} {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {text}") # yellow bg

def fail(text, exitcode):
    print(f"\n{BG.RED}{UTIL.BOLD}[FAIL]{UTIL.RESET} {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {FG.RED}[{exitcode}]{UTIL.RESET} {text}") # red bg
    exit(exitcode)