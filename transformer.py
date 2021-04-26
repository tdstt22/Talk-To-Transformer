from transformers import pipeline, set_seed
from gtts import gTTS

class Transformer:
    
    def __init__ (self):
        self.generator = pipeline('text-generation', model='gpt2')
        set_seed(42)
    
    def run(self, input):
        inp_len = len(input)
        output = self.generator(input, max_length=100, num_return_sequences=1)[0]['generated_text']
        return output
