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
File_ext = ".lfc"



print("Selected to compress.\nEnter the input file")
path_total = input(": ")
file_name = getFileNameFromPath(path_total)

path = getPath(path_total)

print("Enter the path to the output folder")
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

print("Insert the new compressed file name") #if it's blank simply default it to compressed.lfc
new_compr_fn = input(": ")

if (new_compr_fn == ""):
    new_compr_fn = "compressed" #nothing was chosen so change the selected name to compressed, as we default do it

#create the file and write the data to it

createfile = open(new_compr_fn + File_ext, 'w')
createfile.close()
savecomp = open(new_compr_fn + File_ext, 'wb')
savecomp.write(compressed_data)
savecomp.close()



elapsed_time = time.time() - start_time
print("the compression took only:  ", round(elapsed_time),"sec" )

# # i wrote 'elapsed_time' bc i am to lazy to check how
# # to convert miliseconds to seconds, also it is 1:58 
# # GMT+1 so this code could be buggy, but the time.time() thingy works great

print("compression successful app will close in 10 sec")
time.sleep(10)
