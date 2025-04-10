import speech_recognition as sr
import logging

logger = logging.getLogger(__name__)

class STT:

    def __init__(self):
        logger.info("Initializing Speech-to-Text module")
        self.recognizer = sr.Recognizer()

    def run(self, file):
        logger.info("Processing audio file for speech recognition")
        try:
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                logger.debug("Recording audio data from file")
                data = self.recognizer.record(source)
            
            logger.info("Sending audio to Google Speech Recognition")
            text = self.recognizer.recognize_google(data, key=None)
            logger.info(f"Speech recognition successful, transcript length: {len(text)}")
            return text
        except sr.UnknownValueError:
            logger.error("Google Speech Recognition could not understand audio")
            return "Speech recognition failed: Could not understand audio"
        except sr.RequestError as e:
            logger.error(f"Could not request results from Google Speech Recognition service; {e}")
            return f"Speech recognition error: {e}"
        except Exception as e:
            logger.exception(f"Unexpected error in speech recognition: {e}")
            return "Speech recognition failed due to an unexpected error"