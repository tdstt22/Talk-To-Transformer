from flask import Flask, render_template, request, redirect
import speech_recognition as sr
import logging
import os
import sys
from STT import STT
from transformer import Transformer
from TTS import TTS

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('app.log')
    ]
)

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    model_output = ""
    if request.method == "POST":
        logger.info("POST request received")
        if "file" not in request.files:
            logger.warning("No file part in the request")
            return redirect(request.url)
        
        file = request.files["file"]
        logger.info(f"File received: {file.filename}")
        
        response_length = int(request.form["length"])
        logger.info(f"Response length set to: {response_length}")
        
        if file.filename == "":
            logger.warning("Empty filename submitted")
            return redirect(request.url)
        
        if file:
            try:
                # Transcribe the audio file into text
                logger.info("Starting speech-to-text conversion")
                stt = STT()
                transcript = stt.run(file)
                logger.info("Speech-to-text conversion completed")

                # Run the transformer model to get output
                logger.info("Starting transformer model processing")
                model = Transformer()
                model_output = model.run(transcript, response_length)
                logger.info("Transformer model processing completed")

                # Convert transformer text output to audio file
                logger.info("Starting text-to-speech conversion")
                tts = TTS(model_output[len(transcript):])
                tts.save("static/test.mp3")
                logger.info("Text-to-speech conversion completed and saved to static/test.mp3")
            
            except Exception as e:
                logger.error(f"Error processing request: {str(e)}")
                # You might want to handle the error appropriately here

    return render_template("index.html", transcript=transcript, model_output=model_output)

if __name__ == "__main__":
    logger.info("Starting application")
    app.run(host='0.0.0.0', debug=False, threaded=True)