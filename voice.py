import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties for the voice engine (optional)
engine.setProperty('rate', 150)    # Speed of speech
engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Sorry, I did not catch that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""
        return query.lower()

def main():
    speak("Hello! How can I assist you today?")
    while True:
        query = listen()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"Can you be more specific? There are multiple results for {query}.")
            except wikipedia.exceptions.PageError:
                speak("I couldn't find any results on Wikipedia.")
        
        elif 'exit' in query or 'stop' in query:
            speak("Goodbye!")
            break
        
        else:
            speak("I can search Wikipedia for you. Just say, 'Search Wikipedia for...' followed by your query.")

if __name__ == "__main__":
    main()
