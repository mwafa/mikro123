#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
tul = ""
while  tul != "Tutup aplikasi":
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Katakan sesuatu")
	    audio = r.listen(source)
	    
	# recognize speech using Google Speech Recognition
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    tul = r.recognize_google(audio, language='in-ID')
	    print("Kamu berkata:" + tul)
	except sr.UnknownValueError:
	    print("Google Speech Recognition tidak mengerti")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))
