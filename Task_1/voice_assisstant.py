import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

engine.setProperty('rate', 170)


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        speak("Listening")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5)

            print("Recognizing...")
            command = recognizer.recognize_google(audio)

            print("You said:", command)

            return command.lower()

        except sr.WaitTimeoutError:
            speak("I didn't hear anything.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I didn't understand. Please repeat.")
            return ""

        except sr.RequestError:
            speak("Internet connection problem.")
            return ""

        except Exception as e:
            print(e)
            speak("An error occurred.")
            return ""


def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")


def tell_date():
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")


def search_web():
    speak("What would you like me to search for?")

    query = listen()

    if query:
        speak(f"Searching for {query}")
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)


def process_command(command):

    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif "search" in command:
        search_web()

    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye. Have a nice day.")
        return False

    else:
        speak("Sorry, I don't know that command yet.")

    return True


def main():
    speak("Voice Assistant Started")

    running = True

    while running:
        command = listen()

        if command != "":
            running = process_command(command)


if __name__ == "__main__":
    main()