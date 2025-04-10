from transformers import pipeline, set_seed
from gtts import gTTS
import logging

logger = logging.getLogger(__name__)

class Transformer:
    """
    Transformer Class that uses a gpt-2 transformer to output text
    """
    def __init__ (self):
        """
        Initialization method to create transformer object
        """
        logger.info("Initializing Transformer model")
        try:
            logger.info("Loading GPT-2 model")
            self.generator = pipeline('text-generation', model='gpt2')
            logger.info("GPT-2 model loaded successfully")
            set_seed(42)
            logger.debug("Random seed set to 42")
        except Exception as e:
            logger.exception(f"Error initializing transformer model: {e}")
            raise
    
    def run(self, input, length):
        """
        Generate transformer output from input with the desired length
        """
        logger.info(f"Generating text with input length: {len(input)} and max length: {length}")
        try:
            output = self.generator(input, max_length=length, num_return_sequences=1)[0]['generated_text']
            logger.info(f"Text generation successful, output length: {len(output)}")
            return output
        except Exception as e:
            logger.exception(f"Error generating text: {e}")
            raise
