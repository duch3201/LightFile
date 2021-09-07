import os
from os import path
import time
import ctypes
import sys
import zlib
import getopt
import logging
from sys import exit
import traceback

#############################################################################
#                                                                           #
#                                                                           #
#                               LIGHTFILE                                   #
#                                                                           #
#                                                                           #
#############################################################################


################################################################
#                   TODO:
#
#   Re-add ARDT support (maybe even make it better?)
#
#   There are several TODOs all over the file, maybe take a look at them
#   
#   in doAutomation function do:
#   beter exception handeling
#   and make something better
#
################################################################

ctypes.windll.kernel32.SetConsoleTitleW("LightFile") # window title

#logging thing, idk how to describe it
logging.basicConfig(filename='myapp.log', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO,)
logging.basicConfig(filename='LFdebug.log', encoding='utf-8', level=logging.DEBUG)


#main variables
Debug_level = ""         # debug option used for debuging
input_file_path = ""     # name and path of the input file
output_file_path = ""    # name and path of the output file
operation = 3            # the operation, be 0 to compress, 1 to decompress or 2 to configurate lightfile
compress_level =  0      # the bigger the more compressed, at the expense of time to compress


#file variables
history_file = "history.lfh"
chunk_size = 32768
compressed_ext = ".lfc"
input_file = ""
output_file = ""
config_file_name = "config.cfg"
config_file_path = ""
language_folder_name = "lang"

#exceptions
class generalerror(Exception): #use this exception when something really unexpected happen, like something we can't really check for
    def __init__(self):
        logging.critical("a critical error accured, user probably tried to compress a file with a space in the filename")
        ctypes.windll.kernel32.SetConsoleTitleW("LightFile -- :(")
        print("an unknown error accured and the app cannot continue")
        print("if you are seeing this error you probably tried to commpres a file with a space ' ', sadly we don't support files with spaces yet.")
        print("error code: 0")
        time.sleep(5)
        exit()
        #and yes i am aware we could check for spaces in the file name and replace them with "_" but i am too lazy to do that, 
        #also i would probably completely break this while doing that... Too bad!

#class generalerror2(Exception):
 #   def __init__(self):
  #      logging.critical("Something unexpected error")
   #     ctypes.windll.kernel32.SetConsoleTitleW("LightFile -- :(")
    #    print("sorry someting went wrong on our side and the app cannot recover", '\n' "error code: 0")
     #   time.sleep(5)
      #  exit()

class invalidvalueerror(Exception):
    def __init__(self):
        logging.critical("Something unexpected error")
        ctypes.windll.kernel32.SetConsoleTitleW("LightFile -- :(")
        print("an invalid value has been detected, check config files", '\n' "error code: NaN")
        time.sleep(5)
        exit()

class missingconfig(Exception):
    def __init__(self):
        logging.warning("could not find the config files, using defult ones")
        ctypes.windll.kernel32.SetConsoleTitleW("LightFile -- :O")
        print("Sorry but we couldn't find the config files/folder, the app will continue using defult settings", '\n')
        print("with the defult settings the compression level is 6 and debug options are disabled")
        time.sleep(5)
        pass
        

#other variables

light_file_version = "LightFile 1.1"

#keywords to be detected in the getOp() function

validConfigSelectors =        ["o", "config", "configuration"]
validCompressionSelectors =   ["c", "compress", "compression"]
validDecompressionSelectors = ["d", "decompress", "decompression"]

#################

#This loads up the config file
try:
    os.chdir("configs")
    compress_level = open("level.cfg", 'r').read()
    Debug_level = open("debug.cfg", 'r').read()
    os.chdir("..")
    
except:
    #oh it looks like we couldn't find these files, let's notify the user about it and continue with the defult
    compress_level = 6
    Debug_level = False
    raise missingconfig

# refresh the config function
def config_reload():
    global compress_level
    global Debug_level
    #os.chdir("..")
    os.chdir("configs")
   # compress_level.close()
    #Debug_level.close()
    compress_level = "0"
    Debug_level = ""
    compress_level = open("level.cfg", 'r').read()
    Debug_level = open("debug.cfg", 'r').read()
    os.chdir("..")
    return


try:

    ###################
    #checks if the argument op is a valid operation selector and returns accordingly
    #if not valid raises a ValueError exception

    def getOp(op):

    
        for selector in validCompressionSelectors:
            if (op.lower() == selector):
                return 0
    
        for selector in validDecompressionSelectors:
            if (op.lower() == selector):
                return 1

        for selector in validConfigSelectors:
            if (op.lower() == selector):
                return 2
    
        raise ValueError("Not a valid operaton!")

    #####################

    #puts the appropriate values in the main variables
    #from the arguments passed to lightfile in a commandline

    def doAutomation():

        #get the arguments from the sys.argv array
        #starting at 1 because the python file is considered
        #kind of an argument so it would glitch it out

        #options are as following
        #-o is the output file. not strictly nescessary as it will be defaulted to the same as the input one if it doesn't exist
        #-i is the input file. it is nescessary and the program should not run without it.
        #-h is the help option. print out a help message and exit the program
        #-L is the compression level option. not nescessary and will default to 6
        #-c and -d are the operation options for compression and decompression. it is nescessary and the program should not run without it.

        #set globals
        global input_file_path
        global output_file_path
        global operation
        global compress_level
        
        try:
            opts, args = getopt.getopt(sys.argv[1:], "o:i:hL:cd")
        except getopt.GetoptError as msg:
            print(msg)
            exit()

        #loop through every option and do the checks

        #TODO: better exception handling
        #on it!

        try:
            for opt, arg in opts:
                if opt == "-h":
                    #help message argument
                    #just print a help message and exit the program
                    
                    print("-o is the output file. not strictly nescessary as it will be defaulted to the same as the input one if it doesn't exist")
                    print("#-i is the input file. it is nescessary and the program should not run without it.")
                    print("-h is the help option. print out a help message and exit the program")
                    print("-L is the compression level option. not nescessary and will default to 6")
                    print("-c and -d are the operation options for compression and decompression. it is nescessary and the program should not run without it.") 
                    exit()
                if opt == "-L":

                    #compression levle argument
                    #check if it is a number and is inbetween 0 and 9
                    #if it is raise exceptions accordingly otherwise set the compress_level variable to the argument
                    
                    if(int(arg) > 9 or int(arg) < 0):
                        raise ValueError("Value {0} for argument {1} is out of the accepted range.".format(arg, opt))
                    compress_level = int(arg)

                    
                if opt == "-c":

                    #compress operation argument
                    #set operation to compress
                    
                    operation = 0
                if opt == "-d":
                    
                    #decompress operation argument
                    #set operation to decompress
                    
                    operation = 1
                if opt == "-i":

                    #input file argument
                    #set input_file_path to the path provided here

                    input_file_path = arg

                if opt == "-o":

                    #output file argument
                    #set output_file_path to the path provided here

                    output_file_path = arg

            #do a few checks on the data to see if it is valid
            

            #if no operation argument was provided, raise a ValueError exception
            if(operation > 2):
                raise ValueError("You need to select an operation argument!")

            #if the input file path is empty, raise a ValueError exception
            
            if(input_file_path == ""):
                raise ValueError("You need to select an input file!")

            #if the output file path is empty, set it to the input file path

            if(output_file_path == ""):
                output_file_path = input_file_path

            #if there is no '/' or '\' in the input file path then add the current path to it to make it a full path
            #TODO make this better

            current_path = os.getcwd()
            
            if "\\" not in input_file_path:
                input_file_path = current_path + "\\" + input_file_path

            #if there is no '/' or '\' in the input file path then add the current path to it to make it a full path
            #TODO make this better

            if "\\" not in output_file_path:
                output_file_path = current_path + "\\" +output_file_path

            
        except ValueError as msg:
            print(msg)
            exit()

    ###############################################

    #prints the standard config option header and asks the user for an input,
    #returning the user input

    def standardConfigFunction(opt_name, opt_allowed_values, opt_current_value, opt_description):

        #print the standard header for config files
        
        os.system('cls||clear')
        print("---------LIGHTFILE CONFIG---------\n\n")
        
        print("Selected Option: {0}".format(opt_name))
        print("Allowed values: {0}".format(opt_allowed_values))
        print("Current value: {0}".format(opt_current_value))
        print("Description:\n")
        print(opt_description)
        # get the user input and return it
        
        return input("Insert a new value or keep empty if no changes need to be made: ")

        
    #########################
        
    #does the handling of the compression level config selection
    def config_level():
        global compress_level
        os.system('cls||clear')
        os.chdir("configs")

        print("##########|Compress level|##########")

        print("Level 0-9, the current compression level is:", compress_level, " you can change this value for better compression. however higher values may take more time" )
            
        cfglevel = ""
        new_compression_level = 0
        new_compression_level = input(": ") 

        if int(new_compression_level) < 9:
            cfglevel = open("level.cfg", 'w')    


        if int(new_compression_level) > 9:
            raise invalidvalueerror

        cfglevel.write(new_compression_level)
        cfglevel.close()            
        
        os.chdir("..")
        return


    ############################

    #does the handling of the language config selection

    def config_Debug():
        os.system('cls||clear')
        os.chdir("configs")

        print("##########|Debug|##########")

        print("options: true/false ,current value:", Debug_level, '\n' '\n'  "if set to true you will get debug messages")
        
        new_debug_level = input(": ")
        cfgdebug = open("debug.cfg", 'w')
        cfgdebug.write(new_debug_level)
        
        os.chdir("..")
        return

    ###############################################

    #handles the main config window

    def config():
        getting_config = True

        while getting_config == True:

            #reload config
            config_reload()

            #clear the screen again for a better user experience 
            os.system('cls||clear')

            #print the config options
            print(os.getcwd())
            print(compress_level)
            print(Debug_level)

            print("---------{0} config---------\n\n".format(light_file_version))
            print("Available options:\n")
            print("Level -- Level of compression")
            print("Debug -- enters debug mode")
            print("Exit -- Exits the configuration screen")
            print("\n")

            option = input("Insert option: ")

            #check for options and call the according functions
            
            if option == "level":
                config_level()
            if option == "Debug":
                config_Debug()
            if option == "exit":
                getting_config = False
                os.system('cls||clear')
                return


            #write the changes to disk


    ###################

    #puts the appropriate vavlues in the main variables
    #by getting them from the user and 
            
    def doUserInput():
        #clean the screen since we are gonna get
        #the input from the user and
        #it will be cleaner that way

        os.system('cls||clear')
        logging.info("app was started")
        #first off all get the operation
        #using the getOp() function to check if the user input is valid
        #and keep on asking the user until it is fully valid
        print(compress_level)
        print(Debug_level)
        print(os.getcwd())
        
        print("(C)ompression, (D)ecompression or C(O)nfig")
        gettingOp = True
        while (gettingOp == True):
            try:
                global operation
                operation = getOp(input(": "))
            except ValueError as noOp:
                print(noOp)
            else:
                if(operation != 2): #if not config
                    gettingOp = False

                    
                    
                else:
                    config()
                    print("(C)ompression, (D)ecompression or C(O)nfig")
        #now we will get the total file path from the user

        print("Insert the input file (example C:\\ExampleFolder\\ExampleFile.txt)")

        global input_file_path
        
        input_file_path = input(": ")

        #now get the output file path and name

        print("Insert the output file path and name (example C:\\ExampleFolder\\ExampleOutputFile)")

        global output_file_path
        
        output_file_path = input(": ")
        #now we already have enough information to continue, so return

    ####################

    # takes a path to the file to be compressed and the output file
    # compresses the file in chunks and then appends the data to the
    # output file

    def compressFile(inpath, outpath):
        
        cmpr = zlib.compressobj(compress_level)
        try:
            outfile = open(outpath + compressed_ext, "w")
            infile  = open(inpath, "rb")
        except FileNotFoundError:
            print("File {0} does not exist!".format(inpath))
            exit()
        except:
            raise generalerror


        #empty the output file and close it to be reopened in a new mode
        
        outfile.write("")
        outfile.close()

        #reopen it in append mode

        outfile = open(outpath + compressed_ext, "ab")

        #read the first chunk

        data = infile.read(chunk_size)

        #loop through every chunk, compressing and flushing into the file
        #every loop until the entire file was read
        
        while data:
            outfile.write(cmpr.compress(data))
            outfile.flush()
            data = infile.read(chunk_size)

        #write the last bits to the file and close it

        outfile.write(cmpr.flush())
        outfile.close()

    ##########################
    # takes a path to the file to be decompressed and the output file
    # decompresses the file in chunks and then appends the data to the
    # output file

    def decompressFile(inpath, outpath):
        
        dcmpr = zlib.decompressobj()
        try:
            outfile = open(outpath, "w")
            infile  = open(inpath, "rb")
        except FileNotFoundError:
            logging.critical('This file does not exist!')
            print("File {0} does not exist!".format(inpath))
            exit()
        
        #empty the output file and close it to be reopened in a new mode
        
        outfile.write("")
        outfile.close()

        #reopen it in append mode

        outfile = open(outpath, "ab")
        
        
        #read the first chunk

        data = infile.read(chunk_size)

        #loop through every chunk, decompressing and flushing into the file
        #every loop until the entire file was read
        
        while data:
            outfile.write(dcmpr.decompress(data))
            outfile.flush()
            data = infile.read(chunk_size)
            
        #write the last bits to the file and close it
        
        outfile.write(dcmpr.flush())
        outfile.close()
        

    #######################################

    #get the path to the location of the main executable
    #depending on if we're executing through a .py file or through an executable 
    #we will have to use different methods to get it

    if getattr(sys, 'frozen', False): #PyInstaller Executable
        exec_path = sys.executable
    else: # on a .py file
        exec_path = getattr(sys, '_MEIPASS', __file__)

    #now get the path to the installation directory from the path to the main executable
    #and then create the path to the history file and config file

    exec_path, exec_file_name = os.path.split(exec_path)
    history_path = exec_path + "\\" + history_file
    config_file_path = exec_path + "\\" + config_file_name

    #then we are going to call the config load function to
    #load the appropriate variables.

    #config_load()

    #now that we loaded the config into the correct variables,
    #we will load the language lines from the appropriate file



    #check if there are any arguments
    #if there are, get the information from the arguments
    #otherwise go with the user input inside the app

    if(len(sys.argv) > 1):
        doAutomation()
    else:
        doUserInput()

    #now check whether we are compressing or decompressing
    #and call the function accordingly

    start_time = time.time() # time so we can get the elapsed seconds later 

    if(operation == 0):
        compressFile(input_file_path, output_file_path)
        
        #since we are doing compression,
        #write the path to the history file
        try:
            history_file = open(history_path, "w")
        except:

            #if not found print an error message and continue with executing the program
            
            print("an error occured while opening the history ({0}) file!".format(history_path))
        else:

            #write the path

            history_file.write(input_file_path) 
            history_file.close()
            
            
    else:
        decompressFile(input_file_path, output_file_path)


    #print the elapsed time rounded to two decimal points in second

    print("Elapsed time: {0} seconds".format(round(time.time() - start_time, 2)))
except KeyboardInterrupt:
    logging.critical('user pressed ctrl+C, application terminated')
    print("keybord interupt deteced!")
except:
    if Debug_level == True:
        traceback.print_exc()
    else:
        raise generalerror2