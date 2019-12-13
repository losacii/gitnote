import pyttsx3
import sys
engine = pyttsx3.init()

index = 0
def onStart(name):
    global index
    index = 0
    sys.stdout.write('\n')

def onWord(name, location, length):
    global index
    sys.stdout.write(name[index:location+length])
    sys.stdout.flush()
    index = location + length

def onEnd(name, completed):
    sys.stdout.write(name[index:])
    sys.stdout.write('\n')

voices = engine.getProperty('voices')
count = 0
for voice in voices:
    count += 1
    if 'english' in voice.id:
        print("{} : {}".format(count, voice.id))

engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)

engine.setProperty('rate', 160)
engine.setProperty('voice', 'english')


def say(text):
    engine.say(text, name=text)
    engine.runAndWait()
    engine.stop()

text = "The crazy fox jumped over the lazy dog.\nnormal mode, and FAST MODE!"

say(text)

