import os

os.chdir("config")
config_languages = open("languages.txt", 'r')
config_languages = open("languages.txt", 'w') #Oh god why?
print("what language do you want the app to use?")
print("english=ENG, polish=PL")
config1 = input(": ")

if(config1 == "ENG"):
    config_languages.write("ENG")

if(config1 == "PL"):
    config_languages.write("PL")

#oh god how the f*** did that work?