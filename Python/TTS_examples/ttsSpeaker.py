import pyttsx3
import sys
import threading


class Speaker(object):
    def __init__(self):
        self.engine = pyttsx3.init()
        self.index = 0

    def onStart(self, name):
        self.index = 0
        sys.stdout.write('\n')

    def onWord(self, name, location, length):
        sys.stdout.write(name[self.index:location])
        sys.stdout.write(name[location:location+length])
        self.index = location + length
        sys.stdout.flush()

    def onEnd(self, name, completed):
        sys.stdout.write(name[self.index:])
        sys.stdout.write('\n')

    def show_English_voices(self):
        self.voices = self.engine.getProperty('voices')
        count = 0
        print("\n TTS - English Voices:")
        for voice in voices:
            count += 1
            if 'english' in voice.id:
                print("\t{} : {}".format(count, voice.id))

    def engineReady(self):
        # bind events callback
        self.engine.connect('started-utterance', self.onStart)
        self.engine.connect('started-word', self.onWord)
        self.engine.connect('finished-utterance', self.onEnd)

        # Set voice property
        self.engine.setProperty('rate', 160)
        self.engine.setProperty('voice', 'english')

    def say(self, text):
        self.engine.say(text, name=text)
        self.engine.runAndWait()

    def tts(self, text):
        t = threading.Thread(target=self.say, args=(text,))
        t.start()


def mainTest():

    text = """
    The crazy fox jumped over the lazy dog, normal mode, and FAST MODE!"
    Hello World!
    """
    text1 = 'Hello world! good to see you!'

    speaker = Speaker()
    speaker.engineReady()
    speaker.say("hello world!")
    speaker.say(text)


if __name__ == "__main__":
    mainTest()
