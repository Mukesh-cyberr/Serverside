
import json
import string
import os
import pyttsx3
from thefuzz import fuzz, process

import message_generator as mg

def SpeakText(command):
    print(command)
    engine = pyttsx3.init()
    engine.setProperty('rate',210)
    engine.say(command) 
    engine.runAndWait()

with open("contacts.json", 'r') as f:
    contacts = json.load(f)



def parse_command(user_command):
    

    words_list = user_command.translate(str.maketrans('', '', string.punctuation)).split()
    words_list = [word.lower() for word in words_list]
    
    if "whatsapp" in words_list:
        found = False
        for name in contacts.keys():
            for words in words_list:
                if fuzz.ratio(name.lower(), words) > 80:
                    person_name = name
                    found = True
                    break
        if found == False:
            SpeakText(f"Contact '{name}' not found either in the command or the contacts database.")
            exit(1)
        if "message" in words_list:
            separators = ["that", "as", "about"]
            messgen = None
            for sep in separators:
                if sep in user_command:
                    messgen = user_command.split(sep, 1)[1].strip()
                    break
            if messgen is None:
                print("User did not specify a message.")
                exit(3)
            if separators[2] in words_list:
                mssgtype = 0
            else:
                mssgtype = 1
            parsed = {
                "action": "send_message",
                "platform": "whatsapp",
                "contact_name": person_name,
                #Using Locally running Deepseek
                # "message": mg.messagegener(messgen, person_name, mssgtype)

                #Using API
                "message": mg.message_generator_api(messgen, person_name, mssgtype)
            }
        elif "video" in words_list:
            parsed = {
                "action": "video_call",
                "platform": "whatsapp",
                "contact_name": person_name,
            }
        elif "call" in words_list:
            parsed = {
                "action": "call",
                "platform": "whatsapp",
                "contact_name": person_name,
            }
        else:
            os.system("start whatsapp:")


    elif "notepad" in words_list:
        if "write" in words_list:
            s = words_list.index("write") + 1
            write_query = " ".join(words_list[s:])
            filepath = "notes/notes.txt"
            with open(filepath, 'w', encoding='utf-8') as file:
                msg = mg.message_generator_api (write_query, 'notepad and not on ', 0)
                file.write(msg.replace('"', ''))
            os.system(f"start notepad {filepath}")
        else:
            os.system("start notepad")
    elif "youtube" in words_list:
        if "search" in words_list:
            s = words_list.index("search") + 1
            search_query = " ".join(words_list[s:])
            os.system(f"start zen https://www.youtube.com/results?search_query={search_query.replace(' ','+')}")
        else:
            os.system("start zen https://www.youtube.com")

    elif "browser" in words_list:
        if "search" in words_list:
            s = words_list.index("search") + 1
            search_query = " ".join(words_list[s:])
            os.system(f"start zen https://www.google.com/search?q={search_query.replace(' ','+')}")
        else:
            os.system("start zen")
            
    elif 'spotify' in words_list:
        if 'search' in words_list:
            s=words_list.index("search")+1
            search_query=" ".join(map(str,words_list[s:]))
            SpeakText(f"Opening Spotify and searching for {search_query}")
            os.system(f"start zen https://open.spotify.com/search/{search_query.replace(' ','+')}")

    return parsed