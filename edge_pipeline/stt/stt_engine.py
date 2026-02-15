import os
import json
from vosk import Model, KaldiRecognizer


class STTEngine:
    """
    Offline Speech-to-Text using Vosk.
    Designed for CPU-only edge systems.
    """

    def __init__(self, model_path, sample_rate=16000):
        if not os.path.exists(model_path):
            raise FileNotFoundError("Vosk model path not found.")

        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, sample_rate)

    def process_chunk(self, audio_chunk):
        if self.recognizer.AcceptWaveform(audio_chunk):
            result = json.loads(self.recognizer.Result())
            return result.get("text", "")
        return None

    def final_result(self):
        result = json.loads(self.recognizer.FinalResult())
        return result.get("text", "")
