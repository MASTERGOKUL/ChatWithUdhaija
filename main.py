import streamlit as st
import speech_recognition as sr # it needs pyaudio
import time
from time import ctime
from gtts import gTTS
import playsound # it needs PyObjC in mac , i used pipwin for it # a big draw back if it comes to the web
import os
import random

def record_audio():
    with sr.Microphone() as source: # say input from the microphone
        audio = r.listen(source) # it will get the audio input

        # there is a common exception it will through to us , it will show when it doesnot understand the input , like noise
        try:
            voice_data = r.recognize_google(audio) # it will give the audio to recognize_google -> there are more like this
        except sr.UnknownValueError:
            assistant_speak("sorry, I did not get that,could you say it again")
            voice_data=record_audio()
        except sr.RequestError:
            assistant_speak("Sorry , my speech is down now")
        return voice_data

def assistant_speak(audio_string):
    time.sleep(1)
    tts = gTTS(text=audio_string,lang='en') #gtts is used to convert the string to audio
    r = random.randint(1,1000000) # just picking up some random name here to make a name for the file
    audio_file = 'audio-'+str(r) + '.mp3'
    tts.save(audio_file) #it just return an audio we can only able to save that it does not have any speaker modules
    playsound.playsound(audio_file) # play the audio using the playsound library
    print(audio_string)
    os.remove(audio_file) # it is not necessary to have the file so we can delete the saved audio

if __name__ == "__main__":
    r = sr.Recognizer()  # initializing the recognizer

    pre_defined_questions = {"Name":"May I know your good Name ?", "Age":"And how old are you?", "Place":"Where are you residing?"}
    st.title("chatWithQA 🎙️")
    start_btn = st.button("start the conversation 🚀")
    answers = dict()
    if start_btn:
        time.sleep(1)
        welcome_text = "How can i help you ?"
        start_time = ctime()
        print("How can i help you ?")
        a=1
        for question in pre_defined_questions:
            st.write("Question "+str(a) +" 🎤 : "+pre_defined_questions[question])
            assistant_speak(pre_defined_questions[question])
            voice_data = record_audio()
            print(voice_data)
            st.write("Answer "+str(a) +"  👍 : "+voice_data)
            answers[question]=voice_data
            a+=1
        st.balloons()
        assistant_speak("I'm grateful for your insightful responses!")
        end_time = ctime()
        print(start_time,end_time)
        print(answers)
        st.subheader("Information")
        for i in answers:
            st.write(i+" : "+answers[i])
