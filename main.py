from flask import Flask, render_template, request, redirect
import speech_recognition as sr
from STT import STT
from transformer import Transformer
from TTS import TTS

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    model_output = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")
        if "file" not in request.files:
            # Check if file exist
            return redirect(request.url)
        file = request.files["file"]
        response_length = int(request.form["length"])
        if file.filename == "":
            # Check if nothing in file
            return redirect(request.url)
        if file:
            
            # Transcribe the audio file into text
            stt = STT()
            transcript = stt.run(file)

            # Run the transformer model to get output
            model = Transformer()
            model_output = model.run(transcript, response_length)

            # Convert transformer text output to audio file
            tts = TTS(model_output[len(transcript):])
            tts.save("static/test.mp3")


    return render_template("index.html", transcript=transcript, model_output=model_output)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, threaded=True)