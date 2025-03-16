from flask import Flask, render_template, request, redirect
import speech_recognition as sr
import logging
from STT import STT
from transformer import Transformer
from TTS import TTS

# Configure logging for the entire application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('app.log')
    ]
)

app = Flask(__name__)

# Get a logger for the main module
logger = logging.getLogger(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    model_output = ""
    
    try:
        if request.method == "POST":
            logger.info("POST request received to process audio")
            
            if "file" not in request.files:
                logger.warning("No file part in the request")
                return redirect(request.url)
            
            file = request.files["file"]
            response_length = int(request.form["length"])
            
            if file.filename == "":
                logger.warning("No selected file")
                return redirect(request.url)
            
            if file:
                logger.info(f"Processing audio file: {file.filename}")
                
                # Transcribe the audio file into text
                stt = STT()
                transcript = stt.run(file)

                # Run the transformer model to get output
                model = Transformer()
                model_output = model.run(transcript, response_length)

                # Convert transformer text output to audio file
                tts = TTS(model_output[len(transcript):])
                tts.save("static/test.mp3")
                
                logger.info("Audio processing completed successfully")

    except Exception as e:
        logger.error(f"An error occurred during audio processing: {e}")

    return render_template("index.html", transcript=transcript, model_output=model_output)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, threaded=True)
