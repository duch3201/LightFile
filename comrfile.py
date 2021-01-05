import zlib
import sys
import time
import os
 
root_path = '/'
File_ext = ".lfc"
print("please enter a file name")
file_name = input(": ")

print("enter a path to file")
path = input(": ")

print("where do you want to put the compressed file")
output_path = input (": ")

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

start_time = time.time()

print("raw size:", sys.getsizeof(str))

compressed_data = zlib.compress(str, 1)

os.chdir(root_path)
os.chdir(output_path)

print("comppresed size:", sys.getsizeof(compressed_data))

print("do you want to rename the file?")
option = input(": ")

if (option == "yes"):
    print("what do you want to name the compressed file")
    new_compr_fn = input(": ")
    createfile = open(new_compr_fn + File_ext, 'w')
    createfile.close()
    savecomp = open(new_compr_fn + File_ext, 'wb')
    savecomp.write(compressed_data)
    savecomp.close()

if (option == "no"):

    createfile = open('compressed.lfc', 'w')
    createfile.close()
    savecomp = open('compressed.lfc', 'wb')
    #compressed_data.encode("utf8", "ascii")
    savecomp.write(compressed_data)
    savecomp.close()

elapsed_time = time.time() - start_time
print("the compression took only:  ", elapsed_time,"sec" )

# # i wrote 'elapsed_time' bc i am to lazy to check how
# # to convert miliseconds to seconds, also it is 1:58 
# # GMT+1 so this code could be buggy, but the time.time() thingy works great

print("compression successful app will close in 10 sec")
time.sleep(10)