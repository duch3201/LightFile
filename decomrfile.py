#print("hello, world!")

import zlib
import sys
import time
import base64
import os
 
root_path = '/'

file_name = input("please enter a file name:\n")
path = input("enter a path to the compressed file: ")

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


#os.chdir(path)

str = open('file_name', 'br')
try:
    str = open(file_name, 'rb').read()
except FileNotFoundError:
  print("This file does not exist!")

#print(str)

print("compressed size:", sys.getsizeof(str))

decompressed_data = zlib.decompress(str, 2)

print("decomppresed size:", sys.getsizeof(decompressed_data))

os.chdir(root_path)

Print("do you want to rename the compressed file?")

File_rename = input(": ")

    If (file_rename == "yes"):
      Creaternfile = open(file_rename, 'w')
      Creaternfile.close()
      Savecomp = open('decompressed



    If (file_rename == "no")

      createfile = open('decompressed.txt', 'w')
      createfile.close()
      savecomp = open('compressed.txt', 'wb')
      #compressed_data.encode("utf8", "ascii")
      savecomp.write(compressed_data)
      savecomp.close()

os.sleep(10)
