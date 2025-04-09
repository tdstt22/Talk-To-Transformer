from flask import Flask, render_template, request, redirect
import speech_recognition as sr
from STT import STT
from transformer import Transformer
from TTS import TTS
import logging
import os
from datetime import datetime

# Configure logging
log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_filename = os.path.join(log_directory, f"app_{datetime.now().strftime('%Y%m%d')}.log")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
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
        response_length = int(request.form["length"])
        logger.info(f"Response length set to: {response_length}")
        
        if file.filename == "":
            logger.warning("Empty file submitted")
            return redirect(request.url)
        
        if file:
            logger.info(f"Processing file: {file.filename}")
            
            # Transcribe the audio file into text
            logger.info("Starting speech-to-text conversion")
            stt = STT()
            transcript = stt.run(file)
            logger.info(f"Speech-to-text conversion completed. Transcript length: {len(transcript)}")

            # Run the transformer model to get output
            logger.info("Starting transformer model processing")
            model = Transformer()
            model_output = model.run(transcript, response_length)
            logger.info(f"Transformer model processing completed. Output length: {len(model_output)}")

            # Convert transformer text output to audio file
            logger.info("Starting text-to-speech conversion")
            tts = TTS(model_output[len(transcript):])
            tts.save("static/test.mp3")
            logger.info("Text-to-speech conversion completed and saved")

    return render_template("index.html", transcript=transcript, model_output=model_output)

if __name__ == "__main__":
    logger.info("Starting application")
    app.run(host='0.0.0.0', debug=False, threaded=True)