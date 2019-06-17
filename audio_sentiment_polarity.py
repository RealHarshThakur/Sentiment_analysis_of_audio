import speech_recognition as sr 
from textblob import TextBlob                                                      
AUDIO_FILE = ("test.wav") 
r = sr.Recognizer() 
  
with sr.AudioFile(AUDIO_FILE) as source: 
	audio = r.record(source)   
  
try: 
	speech2text=r.recognize_google(audio)
	print("The audio file contains: " +speech2text)
	sentiment=TextBlob(speech2text).sentiment.polarity
	if (sentiment==0):
		print("This was neutral")
	if (sentiment>0):
		print("This was positive")
	if (sentiment<0):
		print("This was negative")
  
except sr.UnknownValueError: 
    print(" Could not understand the audio") 
  
except sr.RequestError as e: 
    print("Could not request results from SpeechRecognition service; {0}".format(e)) 
