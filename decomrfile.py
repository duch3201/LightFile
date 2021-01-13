import zlib
import sys
import time
import base64
import os
import ctypes
from inspect import getsourcefile
from os.path import abspath
ctypes.windll.kernel32.SetConsoleTitleW("LightFile") # this is for the window title

#takes a complete path (example: C:/Users/JohnDoe/Desktop/example.txt) and removes the file name (in this case, C:/Users/JohnDoe/Desktop)

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

#takes a complete path (example: C:/Users/JohnDoe/Desktop/example.txt) and returns just the file name (in this case, example.txt)

# s = string containing the path

def getFileNameFromPath(s):

    #reverse string
    
    reversedstr = ""

    for c in reversed(s):
        reversedstr = reversedstr + c

    #remove the rest of the path, leaving only the file name

    tempfn = ""
    
    for c in reversedstr:
        if(c == '\\' or c == '/'):
            break
        tempfn = tempfn + c
        

    #reverse the file name to make it valid again

    filename = ""
    
    for c in reversed(tempfn):
        filename = filename + c
    
    
    return filename

root_path = '/'
if(len(sys.argv) == 1):
    print("Selected to decompress.\nEnter the input file")
    path_total = input(": ")
    print("Enter the path to the output folder")
    output_path = input (": ")
else:
    path_total = sys.argv[1]
    output_path = getPath(sys.argv[2])
    
file_name  = getFileNameFromPath(path_total)
path       = getPath(path_total)


#change to the input file directory

os.chdir(root_path)
try:
    os.chdir(path)
except FileNotFoundError:
    print("Directory: {0} does not exist!".format(path))
except NotADirectoryError:
    print("{0} is not a directory!".format(path))
except PermissionError:
    print("You do not have permissions to change to {0}".format(path))

#open the file
time_start = time.time()
try:
    str = open(file_name, 'rb').read()
except FileNotFoundError:
  print("This file does not exist!")


#decompress
print("compressed size:", sys.getsizeof(str))

decompressed_data = zlib.decompress(str)

print("decomppresed size:", sys.getsizeof(decompressed_data))

#change to output directory

os.chdir(root_path)
os.chdir(output_path)

#get new filename

if(len(sys.argv) == 1):
    print("Insert the new decompressed file name")
    file_newname = input(": ")
else:
    file_newname = getFileNameFromPath(sys.argv[2])

#open the history file

app_root_path =  getPath(abspath(getsourcefile(lambda:0)))
os.chdir(app_root_path) 
with open('history.lfh') as f:
    mylist = list(f)

#change to the output directory

os.chdir(root_path)
os.chdir(output_path) 

#if nothing was selected as the name default to the one in the history file

if(file_newname == ""):
    file_newname = getFileNameFromPath(mylist[0])

#delete the history file

os.chdir(app_root_path)
os.remove("history.lfh")
os.chdir(output_path)

#create the file and write to it

creaternfile = open(file_newname, 'w')
creaternfile.close()
savedecomp = open(file_newname, 'wb')
savedecomp.write(decompressed_data)
savedecomp.close()

#check if the user wants to delete the compressed file

if(len(sys.argv) == 1):
    print("do you want to delete the compressed file")

    delfile = input(": ")
else:
    delfile = "n"
    
if (delfile == "yes" or delfile == 'y' or delfile == "Y"):
    os.chdir(output_path)
    os.remove(file_name)

#get the elapsed time and print it

time_elapsed = time.time() - time_start
print("decompression only took:", round(time_elapsed), "sec")

#wait 10 seconds and close

if(len(sys.argv) == 1):
    print("decompression successful! app wil close in 10 sec")
    time.sleep(10)
