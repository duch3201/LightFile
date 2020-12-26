#print("hello, world!")

import zlib
import sys
import time
import base64
import os
 
root_path = '/'

file_name = input("please enter a file name:\n")
path = input("enter a path to the compressed file: ")
print("where do you want to put the compressed file")
output_path = input (":  ")

File_rename = "no"
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
#os.chdir(path)

#str = open('file_name', 'br')
try:
    str = open(file_name, 'rb').read()
except FileNotFoundError:
  print("This file does not exist!")

#print(str)

#print(str)

time.sleep(10)

print("compressed size:", sys.getsizeof(str))

decompressed_data = zlib.decompress(str)

print("decomppresed size:", sys.getsizeof(decompressed_data))

os.chdir(root_path)
os.chdir(output_path)


print("do you want to rename the compressed file?")

file_rename = input(": ")

if (file_rename == "yes"):
    creaternfile = open(file_rename, 'w')
    creaternfile.close()
    savedecomp = open(file_rename, 'wb')
    savedecomp.write(decompressed_data)
    savedecomp.close()
#Savecomp = open('decompressed



if (file_rename == "no"):

    createfile = open('decompressed.txt', 'w')
    createfile.close()
    savecomp = open('compressed.txt', 'wb')
    #compressed_data.encode("utf8", "ascii")
    savecomp.write(decompressed_data)
    savecomp.close()


time.sleep(10)
