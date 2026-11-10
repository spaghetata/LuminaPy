#! /usr/bin/env python3

# ==================================================

###########
# imports #
###########

import datetime

# ==================================================

###########
# classes #
###########

class LUMINAPY:
    VERSION     = "1.3.2"
    CREDITS     = "spaghetata"
    LICENSE     = "GPL3.0"
    DISCRIPTION = "This is a small script for error handling"

# ==================================================

class FG:
    BLACK = "\u001b[30m"
    RED = "\u001b[31m"
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33m"
    BLUE = "\u001b[34m"
    PURPLE = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"

# ==================================================

class BG:
    BLACK = "\u001b[40m"
    RED = "\u001b[41m"
    GREEN = "\u001b[42m"
    YELLOW = "\u001b[43m"
    BLUE = "\u001b[44m"
    PURPLE = "\u001b[45m"
    CYAN = "\u001b[46m"
    WHITE = "\u001b[47m"

# ==================================================

class UTIL:
    RESET = "\u001b[0m"
    BOLD = "\u001b[1m"
    ITALICS = "\u001b[3m"
    UNDERLINE = "\u001b[4m"

# ==================================================

###########
#functions#
###########

def info(text):
    print(f"{BG.GREEN}{UTIL.BOLD}[INFO]{UTIL.RESET} {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {text}") # green bg

def warn(text):
    print(f"{BG.YELLOW}{UTIL.BOLD}[WARN]{UTIL.RESET} {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {text}") # yellow bg

def fail(text):
    print(f"{BG.RED}{UTIL.BOLD}[FAIL]{UTIL.RESET} {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {text}") # red bg
    exit(0)