#!/usr/bin/env python3

                ####################
#################   Informations   #################
                ####################

Version     = "1.0.0"
Credits     = "spaghetata"
License     = "GPL3.0"
Discription = "This is a small script for highlighted error handling"

                ####################
#################    Functions     #################
                ####################

def info(message):
    print(f"\033[48;5;34mINFO:\033[0m {message}")

def warning(message):
    print(f"\033[43mWARNING:\033[0m {message}")

def error(message):
    print(f"\033[41mERROR:\033[0m {message}")