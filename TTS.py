from gtts import gTTS
import logging
import os

class TTS:
    def __init__(self, text):
        # Configure logging for the TTS class
        logging.basicConfig(level=logging.INFO, 
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        self.tts = gTTS(text)
    
    def save(self, filename):
        try:
            self.logger.info(f"Attempting to save text-to-speech audio to: {filename}")
            
            # Ensure the directory exists
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            
            self.tts.save(filename)
            
            # Verify file was saved successfully
            if os.path.exists(filename):
                self.logger.info(f"Successfully saved audio file: {filename}")
            else:
                self.logger.warning(f"File save completed, but could not verify: {filename}")
        
        except Exception as e:
            self.logger.error(f"Error saving text-to-speech audio file: {e}")
            raise
