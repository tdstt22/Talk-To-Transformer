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
            return redirect(request.url)
        file = request.files["file"]

        if file.filename == "":
            return redirect(request.url)

        if file:
            """
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            text = recognizer.recognize_google(data, key=None)
            transcript = text
            #print(text)
            """
            stt = STT()
            transcript = stt.run(file)

            model = Transformer()
            model_output = model.run(transcript)

            tts = TTS(model_output[len(transcript):])
            tts.save("static/test.mp3")


    return render_template("index.html", transcript=transcript, model_output=model_output)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, threaded=True)