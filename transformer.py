from transformers import pipeline, set_seed
from gtts import gTTS

class Transformer:
    """
    Transformer Class that uses a gpt-2 transformer to output text
    """
    def __init__ (self):
        """
        Initialization method to create transformer object
        """
        self.generator = pipeline('text-generation', model='gpt2')
        set_seed(42)
    
    def run(self, input, length):
        """
        Generate transformer output from input with the desired length
        """
        output = self.generator(input, max_length=length, num_return_sequences=1)[0]['generated_text']
        return output
