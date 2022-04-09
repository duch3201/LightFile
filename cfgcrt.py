import os


def ConfigCrt(approotpath):
    os.chdir(approotpath)
    os.chdir("config")
    ConfigFile = open("config.cfg", 'w')
    ConfigFile.write("Version: 1.1\n")
    ConfigFile.write("debug: False\n")
    ConfigFile.write("CompressionLevel: 9\n")
    ConfigFile.write("AskUsrForOutputFile: False\n")
    ConfigFile.write("RootPath: {}\n".format(approotpath))
    ConfigFile.close()