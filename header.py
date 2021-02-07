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


ctypes.windll.kernel32.SetConsoleTitleW("LightFile") # window title

#main variables

input_file_path = ""     # name and path of the input file
output_file_path = ""    # name and path of the output file
operation = 0            # the operation, be 0 to compress or 1 to decompress.

#file variables
compressed_ext = ".lfc"
input_file = ""
output_file = ""

#keywords to be detected in the getOp() function

validCompressionSelectors =   ["c", "compress", "compression"]
validDecompressionSelectors = ["d", "decompress", "decompression"]

#checks if the argument op is a valid operation selector and returns accordingly
#if not valid raises a ValueError exception

def getOp(op):

    
    #first loop through the compression selector list
    for selector in validCompressionSelectors:
        if (op.lower() == selector):
            return 0

    #then loop through the decompression selector list
    
    for selector in validDecompressionSelectors:
        if (op.lower() == selector):
            return 1

    #if we reach here, it is not a valid operation selector
    #so raise a ValueError exception
    
    raise ValueError("Not a valid operaton!")

#puts the appropriate values in the main variables
#from the arguments passed to lightfile in a commandline

def doAutomation():
    
    return

#puts the appropriate vavlues in the main variables
#by getting them from the user and 
        
def doUserInput():
    #clean the screen since we are gonna get
    #the input from the player and
    #it will be cleaner that way

    os.system('cls||clear')
    
    #first off all get the operation
    #using the getOp() function to check if the user input is valid
    #and keep on asking the user until it is fully valid
    
    print("(C)ompression or (D)ecompression")
    gettingOp = True
    while (gettingOp == True):
        try:
            global operation
            operation = getOp(input(": "))
        except ValueError as noOp:
            print(noOp)
        else:
            gettingOp = False

    #now we will get the total file path from the user

    print("Insert the input file (example C:\\ExampleFolder\\ExampleFile.txt)")

    global input_file_path
    
    input_file_path = input(": ")

    #now get the output file path and name

    print("Insert the output file path and name (example C:\\ExampleFolder\\ExampleOutputFile)")

    global output_file_path
    
    output_file_path = input(": ")

    #now we already have enough information to continue, so return

# takes a path to the file to be compressed
# and returns the compressed data

def compressFile(path):

    return zlib.compress(open(path, "rb").read())



# takes a path to the file to be decompressed
# and returns the decompressed data

def decompressFile(path):
    
    return zlib.decompress(open(path, "rb").read())

# saves the data in the data variable in a file
# in which the path points to

def saveData(data, path):
    file = open(path, "wb")
    file.write(data)
    file.flush()
    file.close()
    

#######################################

#check if there are any arguments
#if there are, get the information from the arguments
#otherwise go with the user input inside the app

if(len(sys.argv) > 1):
    doAutomation()
else:
    doUserInput()

#now check whether we are compressing or decompressing
#and write to the buffer accordingly

operation_data = ""

start_time = time.time() # time so we can get the elapsed seconds later 

try:
    if(operation == 0):
        operation_data = compressFile(input_file_path)
    else:
        operation_data = decompressFile(input_file_path)

except zlib.error:
    print("An error occured with the selected operation!")
    exit()
except FileNotFoundError:
    print("The file {0} doesn't exist!".format(input_file_path))
    exit()
    #TODO add more exceptions
    
# now that we have the data, save it into a file
# and add the file extension depending on if we are
# compressing or not

if(operation == 0):
    output_file_path = output_file_path + compressed_ext

#TODO EXCEPTIONS

saveData(operation_data, output_file_path)





#print the elapsed time rounded to two decimal points in second

print("Elapsed time: {0} seconds".format(round(time.time() - start_time, 2)))
