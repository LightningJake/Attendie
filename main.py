from transformers import pipeline
import soundfile as sf
import sounddevice as sd

# pip install git+https://github.com/openai/whisper.git
import whisper

# Select from the following models: "tiny", "base", "small", "medium", "large"
model = whisper.load_model("tiny")
results = ""
def voice_rec():
    fs = 48000

    # seconds
    duration = 20
    print("Recording...Just wait a bit")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    # Save as FLAC file at correct sampling rate
    sf.write("my_Audio_file.flac", myrecording, fs)


def transcribe():
    audio = "my_Audio_file.flac"
    print("\nTrancribing...It may take a minute")
    # You can provide the language to the model if it is a bit to "exotic" to predict
    options = {"fp16": False, "language": "English", "task": "transcribe"}
    results = model.transcribe(audio, **options)
    print(results["text"])
    print()
    print("Summary")
    summarizer = pipeline("summarization")
    print(summarizer(results["text"], max_length=50, min_length=20, do_sample=False))

def summary(text):
   pass
    
voice_rec()
transcribe()
