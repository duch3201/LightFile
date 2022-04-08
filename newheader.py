import ctypes
import getopt
import json
import logging
import os
import sys
import time
import traceback
import zlib
from os import path
from sys import exit

import PIL
from flask import Config

#############################################################################
#                                                                           #
#                                                                           #
#                               LIGHTFILE                                   #
#                                                                           #
#                                                                           #
#############################################################################

global LFversion
global IsDebugEnabled
global CompressionLevel
global bAskUsrForOutputFile
global InputFile
global OutputFile
global AllowedOptions
global LowercaseAllowedOptions
global CurrentOperation

LFversion = 0
IsDebugEnabled = False
CompressionLevel = "9"
bAskUsrForOutputFile = False

def ConfigCrt(approotpath):
    ConfigFile = open("config.cfg", 'w')
    ConfigFile.write("Version: 0.1\n")
    ConfigFile.write("debug: False\n")
    ConfigFile.write("CompressionLevel: 9\n")
    ConfigFile.write("AskUsrForOutputFile: False\n")
    ConfigFile.write("RootPath: {}\n".format(approotpath))
    ConfigFile.close()

def loadconfig():
    try:
        approotpath = os.getcwd()
        print(os.getcwd())
        os.chdir("config")
        try:
            ConfigFile = open("config.cfg", 'r')
        except FileNotFoundError:
            print("Config file not found. Creating new config file.")
            ConfigCrt(approotpath)
        ConfigFile = ConfigFile.readlines()
        LFversion = ConfigFile[0].replace("Version: ", "")
        IsDebugEnabled = ConfigFile[1].replace("debug: ", "")
        CompressionLevel = ConfigFile[2].replace("CompressionLevel: ", "")
        bAskUsrForOutputFile = ConfigFile[3].replace("AskUsrForOutputFile: ", "")
    except:
        print("Error loading config file")
        exit()
        


    #return
    #except:
       # print("Error loading config file")
       #exit()

def debug(LFversion, IsDebugEnabled, CompressionLevel, bAskUsrForOutputFile, AllowedOptions, LowercaseAllowedOptions):
    print(LFversion)
    print(IsDebugEnabled)
    print(CompressionLevel)
    print(bAskUsrForOutputFile)
    print(AllowedOptions)
    print(LowercaseAllowedOptions)
    main()
    


def clear():
    if os.name in ('nt', 'dos'):
        command = 'cls'
        os.system(command)
    else:
        command = 'clear'
        os.system(command)

def GatherInfo(bAskUsrForOutputFile, CurrentOperation):
    clear()
    print("#######################|{}|############################ ".format(CurrentOperation)) 
    if CurrentOperation == "Compression":
        InputFile = input("Input file: ")

        
    
    
    
def compr(InputFile, compr_level):
    print("TBD")

def Dcompr(InputFile, compr_level):
    print("TBD")



def main():
    try:
        #print(os.getcwd())
        loadconfig()
        #clear()
        print("#######################|LightFile|############################")
        print("    Choose a option:                                          ")
        print("        C - compression                                       ")
        print("        D - decompression                                     ")
        print("        Co - config                                           ")
        print("        Q - quit                                              ")

        option = input("Option: ")
        AllowedOptions = ["C", "D", "Co", "Q","DEBUG", "c", "d", "co", "q"]
        if option in AllowedOptions:
            if option == "C" or option == "c":
                CurrentOperation = "Compression"
                GatherInfo(bAskUsrForOutputFile, CurrentOperation)
            elif option == "D" or option == "d":
                CurrentOperation = "Decompression"
                GatherInfo(bAskUsrForOutputFile, CurrentOperation)
            elif option == "Co" or option == "co":
                Config()
            elif option == "Q" or option == "q":
                exit()
            elif option == "DEBUG":
                debug(LFversion, IsDebugEnabled, CompressionLevel, bAskUsrForOutputFile, AllowedOptions, LowercaseAllowedOptions)
        if option not in AllowedOptions:
            clear()
            print("Invalid option. Try again.")
            main()
    except KeyboardInterrupt:
        clear()
        print("keyboard interrupt")
        exit()

main()




























#Might be useful later idk |
                        # \/

        #if bAskUsrForOutputFile == True:
            #OutputFile = input("Output file: ")
    #elif:
        #OutputFile = InputFile + ".out"