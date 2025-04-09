from gtts import gTTS
import logging

# Configure logger for TTS class
logger = logging.getLogger(__name__)

class TTS:

    def __init__(self, text):
        logger.info("Initializing TTS module")
        logger.debug(f"Creating gTTS object with text: {text[:50]}{'...' if len(text) > 50 else ''}")
        try:
            self.tts = gTTS(text)
            logger.debug("Successfully created gTTS object")
        except Exception as e:
            logger.error(f"Error creating gTTS object: {str(e)}")
            raise
    
    def save(self, filename):
        logger.info(f"Saving TTS output to file: {filename}")
        try:
            self.tts.save(filename)
            logger.info(f"Successfully saved audio to {filename}")
        except Exception as e:
            logger.error(f"Error saving TTS output to {filename}: {str(e)}")
            raise