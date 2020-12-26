#print("hello, world!")

import zlib
import sys
import time
import base64
import os
 
root_path = '/'

file_name = input("please enter a file name:\n")
path = input("enter a path to the file: ")

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

print("raw size:", sys.getsizeof(str))

decompressed_data = zlib.decompress(str, 2)

print("comppresed size:", sys.getsizeof(compressed_data))

os.chdir(root_path)

createfile = open('compressed.txt', 'w')
createfile.close()
savecomp = open('compressed.txt', 'wb')
compressed_data.encode("utf8", "ascii")
savecomp.write(compressed_data)
savecomp.close()

os.sleep(10)
