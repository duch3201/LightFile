#print("hello, world!")

import zlib
import sys
import time
import base64
import os

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

print("Selected to decompress.\nEnter the input file")
path_total = input(": ")
file_name = getFileNameFromPath(path_total)

path = getPath(path_total)

print("Enter the path to the output folder")
output_path = input (": ")

#File_rename = "no"
os.chdir(root_path)
try:
    os.chdir(path)
except FileNotFoundError:
    print("Directory: {0} does not exist!".format(path))
except NotADirectoryError:
    print("{0} is not a directory!".format(path))
except PermissionError:
    print("You do not have permissions to change to {0}".format(path))

str = open(file_name, 'rb').read()

#str = open('file_name', 'br')
try:
    str = open(file_name, 'rb').read()
except FileNotFoundError:
  print("This file does not exist!")

time_start = time.time()

print("compressed size:", sys.getsizeof(str))

decompressed_data = zlib.decompress(str)
#zobj = zlib.decompressobj(str)  # obj for decompressing data streams that won’t fit into memory at once.

print("decomppresed size:", sys.getsizeof(decompressed_data))

os.chdir(root_path)
os.chdir(output_path)


print("Insert the new compressed file name")

file_newname = input(": ")

#if nothing was inserted default to decompressed.txt

if(file_newname == ""):
    file_newname = "decompressed.txt"

#create the file and write to it

creaternfile = open(file_newname, 'w')
creaternfile.close()
savedecomp = open(file_newname, 'wb')
savedecomp.write(decompressed_data)
savedecomp.close()


time_elapsed = time.time() - time_start

print("decompression only took:", round(time_elapsed), "sec")

print("decompression successful! app wil close in 10 sec")

time.sleep(10)
