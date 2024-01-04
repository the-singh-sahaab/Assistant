# PXWV-GRDT
import speech_recognition as sr
import pyaudio
import win32com.client
import os
import webbrowser
import openai
import datetime
from AppOpener import open
from key_file import apikey
# from key_wali_file import response, prompt_in
import random

speaker = win32com.client.Dispatch("SAPI.SpVoice") 

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
            # print(f"recognized {text}")
            return text
        except Exception as e:
            speaker.Speak("please repeat you request sir")
            bolo()
        # os.system(f"{text}")
chat = ""
def chat_kar(text):
    global chat
    openai.api_key = apikey
    chat += f"shubham:{text}\n jarvi:"
    # prompt_in = "a"
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=chat ,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    # (response['choices'][0]['text'])
    
    chat += f"{response['choices'][0]['text']}\n"
    speaker.Speak(response['choices'][0]['text'])
    # return response['choices'][0]['text']
    print(chat)

    

def ai(prompt):
    openai.api_key = apikey
    text = f'openAI responce for Prompt: {prompt}\n ********************************\n\n'
    
    prompt_in = "a"
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    print(response['choices'][0]['text'])
    speaker.Speak(response['choices'][0]['text'])
    text += response['choices'][0]['text']
    if not os.path.exists("try_project\p8\open_ai"):
        os.mkdir("try_project\p8\open_ai")
    # f = open(f"try_project\p8\open_ai\{prompt[:10]}.txt",'w')#idk q aa rha hai yeh error
    # f.write(f"{text}") #same eerror need to be solved 
        
def website(web):
    sites = [["youtube","https://youtube.com"],["google", "https://www.google.com"]]
    for site in sites:
        if f"search {site[0]}".lower() in text:
            speaker.Speak("working on the request")
            webbrowser.open(site[1])
            
def application(app):
    apps = ["camera", "calculator",'clipchamp','clock','family', 'google chrome', 'instagram', 'legion arena', 'lenovo vantage', 'maps', 'media player', 'microsoft edge','onedrive', 'onenote', 'photos', 'microsoft store', 'microsoft teams', 'microsoft to do', 'visual studio code']
    for app in apps:
        if f"open {app}".lower() in text.lower():
            speaker.Speak("working on the request")
            open(app)
        
print("hey sir")
speaker.Speak("welcome sir  tell me how can i help you")
while True:
    print("listening....")
    text = bolo()
    if "Search " in text:
        website(web = text)
    elif "tell me the time" in text:#strftime tell you the time in whihc formate you want it  
        strftime = datetime.datetime.now().strftime("h%H:%M")
        speaker.Speak(f"sir the time is {strftime}")
    elif "open" in text:
        application(app = text)
    elif "tell me about".lower() in text.lower():
        ai(prompt = text)
    elif "ok stop".lower() in text.lower():
        exit()
    elif 'reset bro'.lower() in text.lower():
        chat = ""
    else:
        chat_kar(text)


# import nltk
# from nltk.stem import WordNetLemmatizer
# lemma = WordNetLemmatizer()

# def lemmatize_words(words):
#     lemmatized_words = []
#     for word in words:
#         lemmatized_word = lemma.lemmatize(word)
#         lemmatized_words.append(lemmatized_word)
#     return lemmatized_words

# sentence = "The quick brown fox jumps over the lazy dog"
# words = nltk.word_tokenize(sentence)
# lemmatized_words = lemmatize_words(words)
# print("Lemmatized Words: ", lemmatized_words)
