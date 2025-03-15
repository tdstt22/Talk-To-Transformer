from flask import Flask, render_template, request, redirect
import speech_recognition as sr
import logging
from STT import STT
from transformer import Transformer
from TTS import TTS

# Configure application-wide logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Output to console
        logging.FileHandler('app.log')  # Output to log file
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    model_output = ""
    if request.method == "POST":
        logger.info("Received POST request")
        if "file" not in request.files:
            logger.warning("No file in request")
            return redirect(request.url)
        
        file = request.files["file"]
        response_length = int(request.form["length"])
        
        if file.filename == "":
            logger.warning("Empty filename")
            return redirect(request.url)
        
        if file:
            try:
                # Transcribe the audio file into text
                stt = STT()
                transcript = stt.run(file)

                # Run the transformer model to get output
                model = Transformer()
                model_output = model.run(transcript, response_length)

                # Convert transformer text output to audio file
                tts = TTS(model_output[len(transcript):])
                tts.save("static/test.mp3")
                
                logger.info("Successfully processed audio and generated response")
            
            except Exception as e:
                logger.error(f"Error processing request: {e}")
                # You might want to add error handling logic here

    return render_template("index.html", transcript=transcript, model_output=model_output)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, threaded=True)
