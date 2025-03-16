import speech_recognition as sr
import logging

class STT:
    def __init__(self):
        # Configure logger for STT class
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Create console handler and set level
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        # Add handler to logger
        self.logger.addHandler(handler)
        
        self.recognizer = sr.Recognizer()
        self.logger.info("STT class initialized")

    def run(self, file):
        try:
            self.logger.info(f"Attempting to transcribe audio file: {file}")
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = self.recognizer.record(source)
            
            self.logger.info("Audio file recorded successfully")
            
            text = self.recognizer.recognize_google(data, key=None)
            
            self.logger.info(f"Transcription successful. Length: {len(text)} characters")
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
