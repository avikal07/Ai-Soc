import time
import os

from edge_pipeline.audio_io.audio_buffer import AudioBuffer
from edge_pipeline.audio_io.wav_stream import WavStream
from edge_pipeline.stt.stt_engine import STTEngine
from edge_pipeline.llm.translator import Translator


def main():
    # Base directory of project
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

    # Paths
    wav_path = os.path.join(BASE_DIR, "demo", "sample_audio", "input.wav")
    stt_model_path = os.path.join(
        BASE_DIR,
        "edge_pipeline",
        "stt",
        "model",
        "vosk-model-small-en-us-0.15"
    )
    llm_model_path = os.path.join(
        BASE_DIR,
        "edge_pipeline",
        "llm",
        "model",
        "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
    )

    print("Initializing streaming + STT pipeline...")

    # Initialize modules
    stream = WavStream(wav_path=wav_path, chunk_size=1024, realtime=True)
    buffer = AudioBuffer()
    stt = STTEngine(model_path=stt_model_path)

    start_time = time.time()

    # Streaming loop
    while True:
        chunk = stream.read_chunk()
        if not chunk:
            break

        buffer.write(chunk)
        buffered_chunk = buffer.read()

        if buffered_chunk:
            text = stt.process_chunk(buffered_chunk)
            if text:
                print("Partial Text:", text)

    # Final STT output
    final_text = stt.final_result()

    end_time = time.time()
    stream.close()

    print("\nFinal Transcription:")
    print(final_text)

    # ---------------- LLM Translation ----------------
    if final_text.strip():
        print("\nLoading translator model...")
        translator = Translator(model_path=llm_model_path)

        translated_text = translator.translate(final_text, target_language="Hindi")

        print("\nTranslated Text:")
        print(translated_text)

    print(f"\nTotal time: {round(end_time - start_time, 2)} seconds")


if __name__ == "__main__":
    main()

