import pyttsx3
import sys
import threading

engine = pyttsx3.init()

# Define: Events Callback
index = 0
def onStart(name):
    global index
    index = 0
    sys.stdout.write('\n')

def onWord(name, location, length):
    global index
    sys.stdout.write(name[index:location])
    sys.stdout.write(name[location:location+length])
    index = location + length
    sys.stdout.flush()

def onEnd(name, completed):
    sys.stdout.write(name[index:])
    sys.stdout.write('\n')

# Show English Voices
voices = engine.getProperty('voices')
count = 0
print("\n TTS - English Voices:")
for voice in voices:
    count += 1
    if 'english' in voice.id:
        print("\t{} : {}".format(count, voice.id))

# bind events callback
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)

# Set voice property
engine.setProperty('rate', 120)
engine.setProperty('voice', 'english')


def say(text):
    engine.say(text, name=text)
    engine.runAndWait()

def tts(text):
    t = threading.Thread(target=say, args=(text,))
    t.start()

def mainTest():

    text = """
    The crazy fox jumped over the lazy dog, normal mode, and FAST MODE!"
    Hello World!
    """
    text1 = 'Hello world! good to see you!'

    tts(text)

if __name__ == "__main__":
    mainTest()
