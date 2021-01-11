import os
import time
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("LightFile")#this is for the window title

def main():

    print("compress(c) a file, or decompress(d) a file")
    
    keepLooping = True
    while keepLooping == True:
        option = input(": ")
        
        if (option == "compress" or option == 'c' or option == "C"):
            os.system('python comrfile.py')
            keepLooping = False
        elif (option == "decompress" or option == 'd' or option == "D"):
            os.system('python decomrfile.py')
            keepLooping = False
        else:
            print("Invalid option! Please try again.")
       
    #print("The app will close after 10 sec")
    #time.sleep(10)

main()
