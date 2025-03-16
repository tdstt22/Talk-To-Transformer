from gtts import gTTS
import logging
import os

class TTS:
    def __init__(self, text):
        """
        Initialize TTS class with logger
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
        
        self.logger.info(f"Initializing TTS with text of length {len(text)} characters")
        self.tts = gTTS(text)
    
    def save(self, filename):
        """
        Save text-to-speech audio with logging
        """
        try:
            self.logger.info(f"Attempting to save audio to {filename}")
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            
            self.tts.save(filename)
            
            # Verify file was created
            if os.path.exists(filename):
                file_size = os.path.getsize(filename)
                self.logger.info(f"Audio file successfully saved: {filename}, Size: {file_size} bytes")
            else:
                self.logger.warning(f"File save operation completed, but file does not exist: {filename}")
        
        except Exception as e:
            self.logger.error(f"Error saving audio file: {e}")
            raise
