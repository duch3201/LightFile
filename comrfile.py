import zlib
import sys
import time
import os
from datetime import datetime
import ctypes
from inspect import getsourcefile
from os.path import abspath
ctypes.windll.kernel32.SetConsoleTitleW("LightFile") #this is for the window title
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

File_ext = ".lfc"
chunksize = 1024
root_path = '/'

#----|ARDT|----
app_root_path = getPath(abspath(getsourcefile(lambda:0)))
os.chdir(app_root_path)
os.chdir("config")
config_file = open ("languages.txt", 'r')

#----|ARDT config file check|----

if (config_file == "ENG"):
    os.chdir(root_path)
    os.chdir(app_root_path)
    os.chdir("lang")
    line88 = open("88.txt", 'r')
    line90 = open("90.txt", 'r')
    line111 = open("111.txt", 'r')
    line114 = open("114.txt", 'r')
    line117 = open("117.txt", 'r')
    line125 = open("125.txt", 'r')
    line129 = open("129.txt", 'r')
    line140 = open("140.txt", 'r')
    line145 = open("145.txt", 'r')
    line151 = open("151.txt", 'r')
    line181 = open("181.txt", 'r')
    line194 = open("194.txt", 'r')
    line212 = open("212.txt", 'r')


if(config_file == "PL"):
    os.chdir(root_path)
    os.chdir(app_root_path)
    os.chdir("lang")
    line88 = open("88.txt", 'r')
    line90 = open("90.txt", 'r')
    line111 = open("111.txt", 'r')
    line114 = open("114.txt", 'r')
    line117 = open("117.txt", 'r')
    line125 = open("125.txt", 'r')
    line129 = open("129.txt", 'r')
    line140 = open("140.txt", 'r')
    line145 = open("145.txt", 'r')
    line151 = open("151.txt", 'r')
    line181 = open("181.txt", 'r')
    line194 = open("194.txt", 'r')
    line212 = open("212.txt", 'r')



#if no extra arguments give the standard selection
if(len(sys.argv) == 1):
    print(line88.read())
    line88.close()
    path_total = input(": ")
    print(line90.read())
    line90.close()
    output_path = input (": ")
else:
    path_total = sys.argv[1]
    output_path = getPath(sys.argv[2])

path = getPath(path_total)
file_name = getFileNameFromPath(path_total)
    
did_find_file = True
file_found_time = datetime.now

#change to the system root path

os.chdir(root_path)

#try changing to the path of the file

try:
    os.chdir(path)
except FileNotFoundError:
    print(line111.read().format(path))
    line111.close()
    time.sleep(10)
except NotADirectoryError:
    print(line114.read().format(path))
    line114.close()
    time.sleep(10)
except PermissionError:
    print(line117.read().format(path))
    line117.close()
    time.sleep(10)

#read the file

try:
    str = open(file_name, 'rb').read()

except FileNotFoundError:
    logging.critical('This file does not exist!')
    print("This file does not exist!")

#somewhere here i noticed a memory leak, Too Bad!

start_time = time.time()

print("raw size:", sys.getsizeof(str))

compressed_data = zlib.compress(str, 9)

#change to the output location

did_compress = True

os.chdir(root_path)
os.chdir(output_path)

print(line140.read(), sys.getsizeof(compressed_data))
line140.close()
#ask for name if not automated

if(len(sys.argv) == 1):
    print(line145.read()) #if it's blank simply default it to compressed.lfc
    new_compr_fn = input(": ")
else:
    new_compr_fn = getFileNameFromPath(sys.argv[2])

if (new_compr_fn == ""):
    new_compr_fn = "compressed" #nothing was chosen so change the selected name to compressed, as we default do it

#create the file and write the                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      to it

createfile = open(new_compr_fn + File_ext, 'w')
createfile.close()
savecomp = open(new_compr_fn + File_ext, 'wb')
savecomp.write(compressed_data)
savecomp.close()

did_save_compressed_file = True


#history file
histfileopn = "history.lfh"

os.chdir(app_root_path)
current_datetime = datetime.now()
current_time = datetime.now().time()

# creating / opening the historu.lfh file

history = open(histfileopn, 'w')
history.write(path_total)
history.close()

#delete the file if the user wants.

if(len(sys.argv) == 1):
    print(line151.read())
    line151.close()
    delfile = input(": ")
else:
    delfile = "n"
    did_delete_file = False

if (delfile == "yes" or delfile == 'y' or delfile == "Y"):
    os.chdir(output_path)
    os.remove(file_name)
    did_delete_file = True

# print elapsed time
elapsed_time = time.time() - start_time
print(line181.read(), round(elapsed_time),"sec" )
line181.close()

#get path for the documents folder
os.path.expanduser(documents)
os.chdir(documents_path)
if(path.exist(documents_path + "LightFileLogs")):
    #enter the directory
    os.chdir("lightFileLogs")
    logfile = logging.basicConfig(filename="logfilename.log", level=logging.INFO)
    logfilesave = open("latest.txt", 'rw')
else:
    #create the directory for logs
    mkdir("LightFileLogs")
    os.chdir("lightFileLogs")
    logging.basicConfig(filename="logfilename.log", level=logging.INFO)
    logfilesave = open("latest.txt", 'rw')


#wait 10 seconds and close if not run by commandline

if(len(sys.argv) == 1):
    print("compression successful app will close in 10 sec")
    time.sleep(10)


#EOF