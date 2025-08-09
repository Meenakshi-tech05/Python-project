import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

try:
    # Reading Microphone as source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        
        print("Talk now, I am listening...")
        audio_text = r.listen(source, timeout=5)  # Listen for 5 seconds or until speaking stops
        
        print("Processing the audio...")
        
        # Recognize the speech using Google Speech Recognition
        try:
            print("Text: " + r.recognize_google(audio_text))
        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
except Exception as e:
    print("Error: {0}".format(e))
