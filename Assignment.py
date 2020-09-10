# 1) Speech to text Api
import speech_recognition as first
import speech_recognition as jr
# 2) Generate text and save it in file
awaz = first.Recognizer()
with first.Microphone() as source:
    print("speak anything: ")
    audio = awaz.listen(source)
    try:
        text = awaz.recognize_google(audio)
      #  print("you said :{}".format(text))
    except:
        print("oops! unclear sound")
        text = "ab kehny ko bacha hi kiya ha"
saveFile = open('speech.txt', 'w')
saveFile.write(text)
saveFile.close()
# 3) finding string from text file
sound = jr.Recognizer()
with jr.Microphone() as sink:
    print("speak dialogue: ")
    audio2 = sound.listen(sink)
    try:
        texty = sound.recognize_google(audio2)
        #print("you said :{}".format(texty))
    except:
        print("oops! unclear sound")
with open('speech.txt', 'r') as readfile:
    file_content = readfile.readline()

print(texty in file_content)
