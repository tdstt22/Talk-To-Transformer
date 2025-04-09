import speech_recognition as sr
import logging

# Configure logger for STT class
logger = logging.getLogger(__name__)

class STT:

    def __init__(self):
        logger.info("Initializing STT module")
        self.recognizer = sr.Recognizer()

    def run(self, file):
        logger.info(f"Processing audio file: {file.filename if hasattr(file, 'filename') else 'unknown'}")
        try:
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                logger.debug("Recording audio data from source")
                data = self.recognizer.record(source)
            
            logger.debug("Attempting to recognize speech using Google Speech Recognition")
            text = self.recognizer.recognize_google(data, key=None)
            logger.info(f"Successfully transcribed audio to text: {text[:50]}{'...' if len(text) > 50 else ''}")
            return text
        except sr.UnknownValueError:
            logger.error("Google Speech Recognition could not understand audio")
            raise
        except sr.RequestError as e:
            logger.error(f"Could not request results from Google Speech Recognition service; {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error during speech recognition: {str(e)}")
            raise