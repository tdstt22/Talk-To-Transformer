from gtts import gTTS
import logging

# Configure logging for TTS module
logger = logging.getLogger('TTS')

class TTS:

    def __init__(self, text):
        logger.info("Initializing Text-to-Speech module")
        try:
            logger.debug(f"Creating gTTS object with {len(text)} characters of text")
            self.tts = gTTS(text)
            logger.info("TTS object created successfully")
        except Exception as e:
            logger.error(f"Error initializing TTS with text: {e}")
            raise
    
    def save(self, filename):
        logger.info(f"Saving TTS audio to file: {filename}")
        try:
            self.tts.save(filename)
            logger.info(f"Successfully saved audio to {filename}")
        except Exception as e:
            logger.error(f"Error saving TTS audio to {filename}: {e}")
            raise