import speech_recognition as sr
import logging

class STT:
    def __init__(self):
        # Configure logging for the STT class
        logging.basicConfig(level=logging.INFO, 
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        self.recognizer = sr.Recognizer()

    def run(self, file):
        try:
            self.logger.info(f"Starting speech recognition for file: {file}")
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = self.recognizer.record(source)
            
            text = self.recognizer.recognize_google(data, key=None)
            self.logger.info(f"Speech recognition successful. Transcribed text: {text}")
            return text
        
        except sr.UnknownValueError:
            self.logger.error("Google Speech Recognition could not understand the audio")
            raise
        
        except sr.RequestError as e:
            self.logger.error(f"Could not request results from Google Speech Recognition service; {e}")
            raise
        
        except Exception as e:
            self.logger.error(f"Unexpected error during speech recognition: {e}")
            raise
