import zlib
import sys
import time
import base64
import os
 
root_path = '/'

file_name = input("please enter a file name:\n")
path = input("enter a path to the file: ")
print("where do you want to put the compressed file")
output_path = input (":  ")

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

#str = open('file_name', 'br')
try:
    str = open(file_name, 'rb').read()
except FileNotFoundError:
  print("This file does not exist!")

#print(str)

print("raw size:", sys.getsizeof(str))

compressed_data = zlib.compress(str, 5)

os.chdir(root_path)
os.chdir(output_path)

print("comppresed size:", sys.getsizeof(compressed_data))

createfile = open('compressed.lfc', 'w')
createfile.close()
savecomp = open('compressed.lfc', 'wb')
#compressed_data.encode("utf8", "ascii")
savecomp.write(compressed_data)
savecomp.close()

print("compression successful app will close in 10 sec")
time.sleep(10)