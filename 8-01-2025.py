#!/usr/bin/env python
# coding: utf-8
!pip install SpeechRecognition pyttsx3 pyaudio
# In[2]:


import pyttsx3
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def main():
    speak("Hello! I am your simple bot from Mallareddy college.")
    speak("you can say hello, ask my name, or say goodbye.")
    while True:
        command=input("you: ").lower()
        if "hello" in command:
            speak("Hi there! Welcome to mallareddy college.")
        elif "what's your name" in command or "what is your name" in command:
            speak("My name is Simple Bot from Mallareddy college.")
        elif "goodbye" in command:
            speak("Goodbye! Have a great day at Mallareddy college.")
            break
        else:
            speak("I didn't understand that.Please try again.")
if __name__=="__main__":
    main()


# In[ ]:




