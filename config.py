import os

#short name that will be used and long name.

languages_short = ["ENG", "PL", "POR"]
languages_long  = ["English", "Polish", "Portuguese"]

print("what do you want to change?" '\n' "language(1), enable multi threading(2), enable multi threading for large files only(3)")
config_option = input(": ")

if (config_option == "1"):

    os.chdir("config")
    config_languages = open("languages.txt", 'r')
    config_languages = open("languages.txt", 'w') #Oh god why?
    config_languages = open("languages.txt", 'w')
    print("what language do you want the app to use?")
    print("english=ENG, polish=PL")

    for i in range(0, len(languages_short)):
        print(languages_short[i] + " = " + languages_long[i])

    config1 = input(": ")

    if(config1 == "ENG"):
        config_languages.write("ENG")
        print("set the language to english")
        exists = False

    for lang in languages_short:
        if(config1 == lang):
            exists = True
            config_languages.write(lang)

    if(exists == False):
        print("Couldn't find that language!")
        config_languages.write(languages_short[0])

    if(config1 == "PL"):
        config_languages.write("PL")
    config_languages.flush()

if (config_option == "2"):
    os.chdir("config")
    enable_mt_config = open("emt.txt", 'r')
    enable_mt_config = open("emt.txt", 'w')
    enable_mt_config.write("True")
    enable_mt_config.close()

if (config_option == "3"):
    os.chdir("config")
    enable_mt_for_lf_config = open("emtfl.txt", 'r')
    enable_mt_for_lf_config = open("emtfl.txt", 'w')
    enable_mt_for_lf_config.write("True")
    enable_mt_for_lf_config.close()


