import speech_recognition as sr
import logging

# Configure logging for STT module
logger = logging.getLogger('STT')

class STT:

    def __init__(self):
        logger.info("Initializing Speech-to-Text module")
        self.recognizer = sr.Recognizer()

    def run(self, file):
        logger.info(f"Processing audio file for speech recognition")
        try:
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                logger.debug("Recording audio data from file")
                data = self.recognizer.record(source)
            
            logger.info("Recognizing speech using Google Speech Recognition")
            text = self.recognizer.recognize_google(data, key=None)
            logger.info(f"Speech recognition successful: {len(text)} characters transcribed")
            return text
        except sr.UnknownValueError:
            logger.error("Google Speech Recognition could not understand audio")
            raise
        except sr.RequestError as e:
            logger.error(f"Could not request results from Google Speech Recognition service; {e}")
            raise