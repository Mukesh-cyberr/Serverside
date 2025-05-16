import datetime
import time
import pyautogui
import os
import json
import emoji
import urllib.parse


with open('contacts.json', 'r') as f:
    contacts = json.load(f)

def send_whatsapp_message(contact_number, message):
    
    print(f"'{emoji.replace_emoji(message, replace = "")}'")
    msg = urllib.parse.quote_plus(message)
    time.sleep(2)
    os.system(f"start whatsapp://send?phone=91{contact_number}^&text={msg}")
    pyautogui.hotkey('tab')
    time.sleep(3)
    
    pyautogui.press('enter')
    breakpoint




def make_call(contact_name):
    print(f" Making WhatsApp voice call to {contact_name}")
    contact_number = contacts.get(contact_name)
    os.system(f"start whatsapp://send?phone=91{contact_number}")
    tab=13
    time.sleep(2)                                       

    for _ in range(tab):                                                    
        
        pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('enter')


def make_video_call(contact_name):
    print(f" Making WhatsApp video call to {contact_name}")
    contact_number = contacts.get(contact_name)
    os.system(f"start whatsapp://send?phone=91{contact_number}")
    tab=12
    time.sleep(2)                                       

    for _ in range(tab):
        pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('enter')