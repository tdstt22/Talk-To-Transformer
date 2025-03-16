from gtts import gTTS
import logging
import os

class TTS:
    def __init__(self, text):
        # Configure logger for TTS class
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Create console handler and set level
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        # Add handler to logger
        self.logger.addHandler(handler)
        
        self.tts = gTTS(text)
        self.logger.info(f"TTS initialized with text: {text[:50]}... (truncated)")
    
    def save(self, filename):
        try:
            self.logger.info(f"Attempting to save audio to {filename}")
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            
            self.tts.save(filename)
            
            # Verify file was created and get file size
            if os.path.exists(filename):
                file_size = os.path.getsize(filename)
                self.logger.info(f"Audio file saved successfully. File size: {file_size} bytes")
            else:
                self.logger.warning("File was not created despite no exceptions")
        
        except Exception as e:
            self.logger.error(f"Error saving audio file: {e}")
            raise
