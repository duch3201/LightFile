import os

#short name that will be used and long name.

languages_short = ["ENG", "PL", "POR"]
languages_long  = ["English", "Polish", "Portuguese"]

os.chdir("config")
config_languages = open("languages.txt", 'w')
print("what language do you want the app to use?")

for i in range(0, len(languages_short)):
    print(languages_short[i] + " = " + languages_long[i])

config1 = input(": ")

exists = False

for lang in languages_short:
    if(config1 == lang):
        exists = True
        config_languages.write(lang)

if(exists == False):
    print("Couldn't find that language!")
    config_languages.write(languages_short[0])

config_languages.flush()

