import speech_recognition as sr
import logging

class STT:
    def __init__(self):
        """
        Initialize STT class with logger
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Create console handler and set level to INFO
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        
        # Add console handler to logger
        self.logger.addHandler(console_handler)
        
        self.recognizer = sr.Recognizer()

    def run(self, file):
        """
        Convert audio file to text with logging
        """
        try:
            self.logger.info(f"Starting speech recognition for file: {file}")
            
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                self.logger.info("Recording audio source")
                data = self.recognizer.record(source)
            
            self.logger.info("Attempting to recognize speech")
            text = self.recognizer.recognize_google(data, key=None)
            
            self.logger.info(f"Speech recognition successful. Transcribed text length: {len(text)} characters")
            return text
        
        except sr.UnknownValueError:
            self.logger.error("Could not understand audio")
            raise
        except sr.RequestError as e:
            self.logger.error(f"Could not request results from Google Speech Recognition service; {e}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error during speech recognition: {e}")
            raise
