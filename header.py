import os
import time

def main():

    print("hello do you want to compress a file, or do you want to decompress a file?")

    option = input(": ")

    if (option == "compress"):
        os.system('python comrfile.py')

    if (option == "decompress"):
        os.system('python decomrfile.py')
   
    print("the app will close after 10 sec")
    time.sleep(10)

main()