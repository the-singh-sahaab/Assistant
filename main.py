import speech_recognition as sr
import pyaudio
import win32com.client
import os
import webbrowser
import openai
import datetime
from AppOpener import open
from key_file import apikey
import random



speaker = win32com.client.Dispatch("SAPI.SpVoice") 

def ai(prompt):
    openai.api_key = apikey
    text1 = f"openai response for prompt: {prompt} \n======================================\n\n"
    
    response = openai.Completion.create(
     model="text-davinci-003",
     prompt=prompt,
     temperature=0.7,
     max_tokens=256,
     top_p=1,
     frequency_penalty=0,
     presence_penalty=0
    )
    # print(response['choices'][0]['text'])
    text1 += response['choices'][0]['text']
    if not os.path.exists("open_ai"):
        os.mkdir("open_ai")
    with os.open(f"try_project\p8\open_ai\proppt-{random.randint(1,3245677566)}",'w') as f:
        f.write(text1)   
    
def bolo():
    recog = sr.Recognizer()
    with sr.Microphone() as mic:
        recog.pause_threshold = 0.6
        recog.adjust_for_ambient_noise(mic)
        audio = recog.listen(mic)
        try:
            print("recognize....")
            text = recog.recognize_google(audio, language = "en-in")
            text = text.lower()
            print(f"recognized {text}")
            return text
        except Exception as e:
            speaker.Speak("some error has occured")
        # os.system(f"{text}")

print("hey sir")
speaker.Speak("welcome sir  tell me how can i help you")
while True:
    print("listening....")
    text = bolo() 
    # todo: add more website
    # todo: add feature to play a song
    # todo: add feature to message viva  whatsapp
    # todo: add feature to make a call 
    # todo: feature to take ss of the current screen 
    # todo: add more app to apps list 
    sites = [["youtube","https://youtube.com"],["google", "https://www.google.com"]]
    for site in sites:
        if f"google {site[0]}".lower() in text:
            speaker.Speak("working on the request")
            webbrowser.open(site[1])
        # else:
        #     speaker.Speak(f"{text}")
    if "tell me the time" in text:#strftime tell you the time in whihc formate you want it  
        strftime = datetime.datetime.now().strftime("h%H:%M")
        speaker.Speak(f"sir the time is {strftime}")
    apps = ["camera", "calculator",'clipchamp','clock','family', 'google chrome', 'instagram', 'legion arena', 'lenovo vantage', 'maps', 'media player', 'microsoft edge','onedrive', 'onenote', 'photos', 'microsoft store', 'microsoft teams', 'microsoft to do', 'visual studio code']
    for app in apps:
        if f"open {app}".lower() in text.lower():
            open(app)
    if "use your intelligence".lower() in text.lower():
        ai(prompt=text)
            

    