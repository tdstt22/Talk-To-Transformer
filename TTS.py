from gtts import gTTS

class TTS:

    def __init__(self, text):
        self.tts = gTTS(text)
    
    def save(self, filename):
        self.tts.save(filename)