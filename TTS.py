from gtts import gTTS
import logging

logger = logging.getLogger(__name__)

class TTS:

    def __init__(self, text):
        logger.info("Initializing Text-to-Speech module")
        try:
            logger.debug(f"Creating gTTS object with text length: {len(text)}")
            self.tts = gTTS(text)
            logger.info("gTTS object created successfully")
        except Exception as e:
            logger.exception(f"Error creating gTTS object: {e}")
            raise
    
    def save(self, filename):
        logger.info(f"Saving audio to file: {filename}")
        try:
            self.tts.save(filename)
            logger.info(f"Audio saved successfully to {filename}")
        except Exception as e:
            logger.exception(f"Error saving audio to {filename}: {e}")
            raise