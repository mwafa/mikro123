import speech_recognition as sr

def get_text():
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Katakan sesuatu")
	    audio = r.listen(source)
	    
	# recognize speech using Google Speech Recognition
	try:
	    return r.recognize_google(audio, language='in-ID')
	except sr.UnknownValueError:
		return False
	except sr.RequestError as e:
		print("Error")
		return False
	    # print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == '__main__':
	print(get_text())