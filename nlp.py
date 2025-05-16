import json
import speech_recognition as sr
import pyttsx3


from nlp_parser import parse_command
from whatsapp_bot import send_whatsapp_message, make_call, make_video_call

def SpeakText(command):
    print(command)
    engine = pyttsx3.init()
    engine.setProperty('rate',210)
    engine.say(command) 
    engine.runAndWait()

with open('contacts.json', 'r') as f:
    contacts = json.load(f)

mic = sr.Microphone() # To get the input from the microphone
recognizer = sr.Recognizer() #To recognize the speech

SpeakText("Hello sir! How can I help you?\n")


while True:
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Speak now...")
        audio = recognizer.listen(source)

    try:
        # recognized_text = recognizer.recognize_google(audio)
        recognized_text = "hey jarvis open whatsapp and send message to shiva that I can't come to the meeting"
        print(f"User said: {recognized_text}")

        wake_up_command = ["hey jarvis", "jarvis"]
        for wake in wake_up_command:
            if wake in recognized_text.lower():
                parsed = parse_command(recognized_text)
            
            action = parsed['action']

            if action == 'send_message' and parsed['platform'] == 'whatsapp':
                contact_name = parsed['contact_name']
                message = parsed['message']
                SpeakText(f"Opening WhatsApp and sending message to {contact_name}")
                contact_number = contacts.get(contact_name)
                if contact_number:
                    send_whatsapp_message(contact_number, message)
                    break
                else:
                    print(f"Contact '{contact_name}' not found in contacts.json")

            elif action == 'call' and parsed['platform'] == 'whatsapp':
                contact_name = parsed['contact_name']
                make_call(contact_name)
                break

            elif action == 'video_call' and parsed['platform'] == 'whatsapp':
                print("Exe")
                contact_name = parsed['contact_name']
                make_video_call(contact_name)
    
        
    except sr.UnknownValueError:
        SpeakText("Sorry sir, Could you repeat again?")
        break
    except Exception as e:
        print(f"  Error: {e}")
        break
    break