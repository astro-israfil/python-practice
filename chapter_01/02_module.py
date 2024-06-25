import pyjokes
import pyttsx3

# initialize python text to speech
engine = pyttsx3.init()

# get a random joke text
joke = pyjokes.get_joke("en")

# get speech by pthon text to speech
engine.say(joke)
engine.runAndWait()