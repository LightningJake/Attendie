import sys
from flask import Flask, render_template, request, jsonify
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtCore import pyqtSlot
import soundfile as sf
import sounddevice as sd
import whisper
from transformers import pipeline, AutoTokenizer

model = whisper.load_model("tiny")
tokenizer = AutoTokenizer.from_pretrained("t5-base", model_max_length=512)

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Attendie-AI'
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        duration_label = QLabel('Recording Duration (seconds):', self)
        duration_label.move(20, 20)
        self.duration_entry = QLineEdit(self)
        self.duration_entry.move(200, 20)
        self.duration_entry.resize(100, 20)

        self.start_button = QPushButton('Start', self)
        self.start_button.move(150, 60)
        self.start_button.clicked.connect(self.on_click)

        self.summary_label = QLabel('Trans:', self)
        self.summary_label.move(20, 100)
        self.summary_text = QTextEdit(self)
        self.summary_text.move(20, 120)
        self.summary_text.resize(450, 60)

        self.bullet_label = QLabel('Bullet Points:', self)
        self.bullet_label.move(20, 200)
        self.bullet_text = QTextEdit(self)
        self.bullet_text.move(20, 220)
        self.bullet_text.resize(450, 60)

        self.show()

    @pyqtSlot()
    def on_click(self):
        duration = int(self.duration_entry.text())
        voice_rec(duration)
        summary, bullet_points = transcribe()
        self.summary_text.setText(summary)
        self.bullet_text.setText(bullet_points)

def voice_rec(duration):
    fs = 48000
    print("Recording...")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    sf.write("recording.flac", myrecording, fs)

def transcribe():
    audio = "recording.flac"
    print("\nTranscribing...Please Wait")
    options = {"fp16": False, "language": "English", "task": "transcribe"}
    results = model.transcribe(audio, **options)
    transcription_text = results["text"]
    """ print(results["text"]) """
    print(transcription_text)
    summarizer = pipeline("summarization","t5-base",tokenizer=tokenizer)
    print("Summary")
    list_text = summarizer(results["text"], max_length=55, min_length=20, do_sample=False)
    print(list_text[0].get('summary_text'))
    summary = list_text[0].get('summary_text')
    bullet_points = ""
    for line in summary.split(". "):
        bullet_points += "•" + line.capitalize() +"\n"
    print("BULLET POINTS: ")
    print(bullet_points)
    return transcription_text, bullet_points

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        duration = int(request.form["duration"])
        voice_rec(duration)
        transcription_text, bullet_points = transcribe()
        return render_template("index.html", transcription=transcription_text, bullet_points=bullet_points)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)