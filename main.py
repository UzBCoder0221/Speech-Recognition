import speech_recognition as sr

def recognizSpeech():
    recognizer = sr.Recognizer()
    print("Adjusting for ambient noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source)
    recognizer.pause_threshold = 1.3
    with sr.Microphone() as source:
        print("Listening...")
        audio_data = recognizer.listen(source)
        print("Recognizing...")
        try:
            text = recognizer.recognize_google(audio_data,language='uz')
            print(f"Recognized Speech: {text}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    recognizSpeech()
