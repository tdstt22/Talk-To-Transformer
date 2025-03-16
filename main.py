from flask import Flask, render_template, request, redirect
import speech_recognition as sr
from STT import STT
from transformer import Transformer
from TTS import TTS
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Console output
    ]
)

# Create a logger for the main application
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    model_output = ""
    if request.method == "POST":
        logger.info("POST request received for processing")
        
        if "file" not in request.files:
            logger.warning("No file part in the request")
            return redirect(request.url)
        
        file = request.files["file"]
        response_length = int(request.form["length"])
        
        if file.filename == "":
            logger.warning("No selected file")
            return redirect(request.url)
        
        if file:
            try:
                # Transcribe the audio file into text
                logger.info(f"Starting speech-to-text conversion for file: {file.filename}")
                stt = STT()
                transcript = stt.run(file)

                # Run the transformer model to get output
                logger.info(f"Running transformer model with input: {transcript}")
                model = Transformer()
                model_output = model.run(transcript, response_length)

                # Convert transformer text output to audio file
                logger.info("Converting model output to speech")
                tts = TTS(model_output[len(transcript):])
                tts.save("static/test.mp3")
                
                logger.info("Processing completed successfully")

            except Exception as e:
                logger.error(f"Error in processing request: {e}")
                return "An error occurred during processing", 500

    return render_template("index.html", transcript=transcript, model_output=model_output)

if __name__ == "__main__":
    logger.info("Starting Flask application")
    app.run(host='0.0.0.0', debug=False, threaded=True)
