import os
import time
import ctypes
import sys
import getopt
from inspect import getsourcefile
from os.path import abspath
ctypes.windll.kernel32.SetConsoleTitleW("LightFile")#this is for the window title

def getPath(s):

    #reverse string
    
    reversedstr = ""

    for c in reversed(s):
        reversedstr = reversedstr + c

    #remove the rest of the path, leaving only the file name

    tempfn = ""
    shouldAdd = False
    
    for c in reversedstr:
        if(shouldAdd == True):
            tempfn = tempfn + c
        if(c == '\\' or c == '/'):
            shouldAdd = True
        
        

    #reverse the file name to make it valid again

    filename = ""
    
    for c in reversed(tempfn):
        filename = filename + c
    
    
    return filename

def handleArguments():
    
    
    
    opts, args = getopt.getopt(sys.argv[1:], "hc:d:o:") #get the arguments and sort them out with getopt
    
    cmpOrDcmp = ""
    outputfile = ""
    inputfile = ""

    #loop through every option and check them
    
    for opts, args in opts:
        if opts in("-c", "-d"):
            cmpOrDcmp = opts
            inputfile = args
        elif(opts == "-o"):
            outputfile = args
        elif(opts == "-h"):
            print("lightfile -c (-d for decompression) <input file>  -o <output file>")
            sys.exit()
        else:
            print("Unknown argument: " + opts)
            sys.exit()

    #check if inputs were valid
    
    if(inputfile == ""):
        print("No input file selected!")
        sys.exit()

    if(outputfile == ""):
        print("No output file selected!")
        sys.exit()

    if(cmpOrDcmp == ""):
        print("No operation selected!")


    #check if there is a \ or an / on the files and work accordingly

    if not ("\\" in inputfile or "/" in inputfile):
        inputfile = os.getcwd().replace("\\", "/") + "/" + inputfile

    if not ("\\" in outputfile or "/" in outputfile):
        outputfile = os.getcwd().replace("\\", "/") + "/" + outputfile
        

    #call the files
        
    if(cmpOrDcmp == "-c"):
        os.system('python ' + getPath(abspath(getsourcefile(lambda:0))) + '\\' + 'comrfile.py '   + inputfile + " " + outputfile)
    else:
        os.system('python ' + getPath(abspath(getsourcefile(lambda:0))) + '\\' + 'decomrfile.py ' + inputfile + " " + outputfile)
    sys.exit()
    
    
def main():
    if(len(sys.argv) > 1):
        handleArguments()

    print("compress(c) a file, or decompress(d) a file")
    path = getPath(abspath(getsourcefile(lambda:0)))
    keepLooping = True
    while keepLooping == True:
        option = input(": ")
        
        if (option == "compress" or option == 'c' or option == "C" ):
            os.system('python ' + path + '\\' + 'comrfile.py ')
            keepLooping = False
        elif (option == "decompress" or option == 'd' or option == "D"):
            os.system('python ' + path + '\\' + 'decomrfile.py ')
            keepLooping = False
        else:
            print("Invalid option! Please try again.")
       
    #print("The app will close after 10 sec")
    #time.sleep(10)

main()
