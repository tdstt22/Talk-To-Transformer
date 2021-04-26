import speech_recognition as sr

class STT:

    def __init__(self):

        self.recognizer = sr.Recognizer()

    def run(self, file):
        audioFile = sr.AudioFile(file)
        with audioFile as source:
            data = self.recognizer.record(source)
        text = self.recognizer.recognize_google(data, key=None)
        return text