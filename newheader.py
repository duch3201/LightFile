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

try:
    import cfgcrt
except ImportError:
    print("could not find create config file module!")
    print("don't worry, the app can continue without it")
    input("press anykey to continue")

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

#def ConfigCrt(approotpath):
 #   ConfigFile = open("config.cfg", 'w')
  #  ConfigFile.write("Version: 0.1\n")
   # ConfigFile.write("debug: False\n")
    #ConfigFile.write("CompressionLevel: 9\n")
    #ConfigFile.write("AskUsrForOutputFile: False\n")
    #ConfigFile.write("RootPath: {}\n".format(approotpath))
    #ConfigFile.close()

def loadconfig():
    approotpath = os.getcwd()
    os.chdir(approotpath)
    try:
        #print(os.getcwd())
        #print("1")
        os.chdir("config")
        #print(os.getcwd())
        #print("2")
        try:
            ConfigFile = open("config.cfg", 'r')
        except FileNotFoundError:
            print("Config file not found. Creating new config file.")
            cfgcrt.ConfigCrt(approotpath)
            input("Press anykey to continue")
            loadconfig()
        ConfigFile = ConfigFile.readlines()
        LFversion = ConfigFile[0].replace("Version: ", "")
        print(LFversion)
        input("")
        IsDebugEnabled = ConfigFile[1].replace("debug: ", "")
        #print(IsDebugEnabled)
        #input("")
        CompressionLevel = ConfigFile[2].replace("CompressionLevel: ", "")
        #print(CompressionLevel)
        #input("")
        bAskUsrForOutputFile = ConfigFile[3].replace("AskUsrForOutputFile: ", "")
        #print(bAskUsrForOutputFile)
        #input("")
    except:
        #print("Error loading config file")
        #exit()
        pass


    #return
    #except:
       # print("Error loading config file")
       #exit()

def debug(LFversion, IsDebugEnabled, CompressionLevel, bAskUsrForOutputFile, AllowedOptions):
    clear()
    print("all used variables:")
    print("LFversion: ", LFversion)
    print("IsDebugEnabled: ", IsDebugEnabled)
    print("CompressionLevel", CompressionLevel)
    print("bAskUserForOutputFile: ", bAskUsrForOutputFile)
    print("AllowedOptions: ", AllowedOptions)
    #print(LowercaseAllowedOptions)
    input("Press anykey to continue")
    main(LFversion)
    


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



def main(LFversion):
    try:
        #print(os.getcwd())
        loadconfig()
        #clear()
        print("#######################|LightFile ver: {}|############################".format(LFversion))
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
                if IsDebugEnabled == True:
                    debug(LFversion, IsDebugEnabled, CompressionLevel, bAskUsrForOutputFile, AllowedOptions)
                else:
                    print("Debug is not enabled")
                    input("Press anykey to continue")
                    main(LFversion)
        if option not in AllowedOptions:
            clear()
            print("Invalid option. Try again.")
            input("Press anykey to continue")
            main(LFversion)
    except KeyboardInterrupt:
        clear()
        print("keyboard interrupt")
        exit()

main(LFversion)




























#Might be useful later idk |
                        # \/

        #if bAskUsrForOutputFile == True:
            #OutputFile = input("Output file: ")
    #elif:
        #OutputFile = InputFile + ".out"