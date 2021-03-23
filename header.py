import os
from os import path
import time
import ctypes
import sys
import zlib
import getopt

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

#main variables

input_file_path = ""     # name and path of the input file
output_file_path = ""    # name and path of the output file
operation = 3            # the operation, be 0 to compress, 1 to decompress or 2 to configurate lightfile
compress_level = 6       # the bigger the more compressed, at the expense of time to compress


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
        ctypes.windll.kernel32.SetConsoleTitleW("LightFile -- :(")
        print("an unknown error accured and the app cannot continue")
        print("if you are seeing this error you probably tried to commpres a file with a space ' ', sadly we don't support files with spaces yet.")
        print("error code: 0")
        time.sleep(5)
        exit()
        #and yes i am aware we could check for spaces in the file name and replace them with "_" but i am too lazy to do that, 
        #also i would probably completely broke this while doing that... Too bad!

#class generalerror2(Exception):
 #       ctypes.windll.kernel32.SetConsoleTitleW("LightFile -- :(")
  #      print("sorry someting went wrong on our side and the app cannot recover", '\n' "error code: 0")
   #     time.sleep(5)
    #    exit()


#other variables

#sometimes i sit and wonder, what the hell is wrong with me
light_file_version = "LightFile 2.0 lol i think, im trying to bring back features from the old version and add more so why the hell not go straight to 2.0. also i am the $&*)@^% CEO i can do what ever i want!"

#language variables

language_file = "ENG"
accepted_language_values = ["ENG", "PL", "POR"]
language_list = "English(ENG), Polish(PL), Portuguese(POR)"

# ARDT variables
ARDT_ext = ".lfl"
current_line = 0
ARDT_lines = []

#keywords to be detected in the getOp() function

validConfigSelectors =        ["o", "config", "configuration"]
validCompressionSelectors =   ["c", "compress", "compression"]
validDecompressionSelectors = ["d", "decompress", "decompression"]

###################

#returns the next line in the ARDT list

def ARDT_next():

    global current_line
    global ARDT_lines

    line = ARDT_lines[current_line]

    current_line += 1

    return line
    
###################

#loads the language into ARDT_lines
#to be used in the ARDT_next() function

def ARDT_load_lines(language_file_path):

    global ARDT_lines
    global ARDT_ext

    # im gonna do it the old fashioned way, sorry

    os.chdir("lang")
    line1 = open("line1.lfl", "r")
    print(line1.read())
        
    input()

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
        
    #This code is supposed to be simple
    #but it seems that's not the case
    #These errors is staring back at me
    #half*alive The fall




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
                #TODO add the help message, Done and Done!
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

#################

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

    val = standardConfigFunction("Level", "0-9", compress_level, "The level of compression to be used. Higher values have better compression at the expensive of taking more time to compress\n0 is no compression and 9 is max compression")
    

    #check the values to see if it's empty or is an invalid value
    
    if(val == ""):
        return
    else:
        try:
            val = int(val)
            if val < 0 or val > 9:
                #the user put in an invalid value. simply return
                return
            compress_level = int(val)
        except ValueError:
            #uh oh! the user probably put a letter here. let's not change the compress level
            return

############################

#does the handling of the language config selection



def config_language():

    global language_file

    val = standardConfigFunction("Language", accepted_language_values, language_file, "The language that will be used.\nA restart is required for changes to appear.\n\nCurrent accepted languages are:{0}".format(language_list))
    
    for lang in accepted_language_values:
        if(val.upper() == lang):
            language_file = val.upper()
            break
     
###############################################

#This function loads up the config file
#and the other saves to the config file.
#the config file is as follows:

#  LANGUAGE
#  COMPRESSION LEVEL

# everything is loaded and stored in the correct variables

def config_save():

    #open the config file

    
    file_config = open(config_file_path, "w")

    #write the variables to it
    
    file_config.write(str(language_file) + "\n")
    file_config.write(str(compress_level) + "\n")

    #save it
    
    file_config.close()

def config_load():
    
    #open the config file
    try:
        file_config = open(config_file_path, "r")
    except FileNotFoundError:
        #we didn't find a config file
        #return and let it stay with the default config
        return


    #read the file into the variables

    language_file = file_config.readline().rstrip('\r\n')

    compress_level = int(file_config.readline())

    #then close the file
    
    file_config.close()


###############################################

#handles the main config window

def config():
    getting_config = True

    while getting_config == True:
        #clear the screen again for a better user experience
        
        os.system('cls||clear')

        #print the config options

        print("---------{0} config---------\n\n".format(light_file_version))
        print("Available options:\n")
        print("Level -- Level of compression")
        print("Language -- Language that ligthfile will use")
        print("Exit -- Exits the configuration screen")
        print("\n")

        option = input("Insert option: ")

        #check for options and call the according functions
        
        if option.lower() == "level":
            config_level()
        if option.lower() == "language":
            config_language()
        if option.lower() == "exit":
            getting_config = False
            os.system('cls||clear')


        #write the changes to disk

        config_save()

###################

#puts the appropriate vavlues in the main variables
#by getting them from the user and 
        
def doUserInput():
    #clean the screen since we are gonna get
    #the input from the user and
    #it will be cleaner that way

    os.system('cls||clear')
    
    #first off all get the operation
    #using the getOp() function to check if the user input is valid
    #and keep on asking the user until it is fully valid
    
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

config_load()

#now that we loaded the config into the correct variables,
#we will load the language lines from the appropriate file

language_file_path = exec_path + "\\" + language_folder_name + "\\" + language_file + ARDT_ext

ARDT_load_lines(language_file_path)

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
