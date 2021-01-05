#print("hello, world!")

import zlib
import sys
import time
import base64
import os
 
root_path = '/'

print("please enter a file name")
file_name = input(": ")

print("enter a path to file")
path = input(": ")

print("where do you want to put the decompressed file")
output_path = input (": ")

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


print("do you want to rename the compressed file?")

file_rename = input(": ")

if (file_rename == "yes"):
    print("please enter the whole file name, example [file_name.ext]")
    print("enter new file name")
    file_newname = input("here: ")

    creaternfile = open(file_newname, 'w')
    creaternfile.close()
    savedecomp = open(file_newname, 'wb')
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

time_elapsed = time.time() - time_start

print("decompression only took:", time_elapsed, "sec")

print("decompression successful! app wil close in 10 sec")

time.sleep(10)
