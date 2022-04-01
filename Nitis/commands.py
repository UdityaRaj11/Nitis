from playsound import playsound
from gtts import gTTS
import subprocess
import winapps
from filesaddress import Filesaddress
from get_answers import Fetcher
from Dict_answers import wikiFetcher
from video_audio import VAFetcher


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm", "Ha bhai"]
        self.cancel = ["no", "negative", "negative niteesh", "don't", "wait", "cancel", "bye", "exit", "quit"]

    def respond(self, response):
        language = 'en'
        myobj = gTTS(text=response, lang=language, slow=False)
        myobj.save("RpcSpeech.mp3")
        playsound('./RpcSpeech.mp3')

    def discover(self, text):
        ad = Filesaddress()
        if "what" in text and "name" in text:
            if "my" in text and "name is" not in text:
                self.respond("You haven't told me your name yet")

            else:
                self.respond("My name is niteesh:  How are you?")

        elif "I" in text and "not" not in text and ("fine" in text or "ok" in text or "great" in text or "good" in text):
            self.respond("That's great")
            self.respond("So, What will you like to know?")

        elif "launch" in text or "open" in text:
            application = text.split(" ", 1)[-1]
            self.respond("Opening " + application)
            ad.call_application(application)
            quit()
        elif text in self.cancel:
            self.respond("See you soon, bro.")
            quit()
        elif "what" in text and ("is" in text or "are" in text) and " speed " not in text and " + " not in text and " - " not in text and "capital" not in text:
            removal_list = [" is", " are ", "what", " an ", " a ", " the "]

            for word in removal_list:
                text = text.replace(word, '')

            text = text.replace(" ", "-")
            new_text = text[0].lower() + text[1:]
            print(new_text)
            f1 = wikiFetcher("https://www.oxfordlearnersdictionaries.com/definition/english/"+new_text)
        elif "play" in text:
            removal_list = ["play ", " on "]

            for word in removal_list:
                text = text.replace(word, '')
            if "YouTube" in text:
                text = text.replace("YouTube", '')
                text = text.replace(" ", "+")
                new_text = text[0].lower() + text[1:]
                print(new_text)
                f2 = VAFetcher("https://www.youtube.com/results?search_query="+new_text)
        else:
            #text = text.replace(" ", "-")
            text = text.replace(" ", "+")
            f = Fetcher("https://www.google.co.in/search?q=" + text)
            #f = Fetcher("https://www.bing.com/search?q=" + text)




