# Offline On-Device Speech-to-Speech Semantic Translation (Edge AI)

## Overview

This project implements a fully offline speech translation pipeline that converts spoken audio into semantically equivalent text using only on-device CPU inference.

The system demonstrates how modern AI models can operate in constrained edge environments without GPU acceleration or cloud APIs.

The goal is to simulate a real edge-AI deployment scenario where privacy, latency, and connectivity constraints prevent the use of online services.

---

## Key Features

* Fully offline processing (no internet required after setup)
* CPU-only inference (no GPU acceleration)
* Real-time streaming audio processing
* On-device speech recognition
* Local large language model semantic translation
* Edge-AI oriented architecture
* Model quantization for memory efficiency

---

## System Pipeline

Audio Input → Speech Recognition → Semantic Translation → Output Text

### Components

| Module               | Technology Used                 | Purpose                              |
| -------------------- | ------------------------------- | ------------------------------------ |
| Audio Streaming      | Python WAV streaming            | Simulates real-time microphone input |
| Speech-to-Text       | Vosk Small Model                | Offline transcription                |
| Semantic Translation | TinyLlama 1.1B (Quantized GGUF) | Local language understanding         |
| Runtime              | CPU Only                        | Edge deployment simulation           |

---

## Project Structure

```
speech-to-speech-arm/
│
├── edge_pipeline/
│   ├── audio_io/          # Streaming audio processing
│   ├── stt/               # Speech recognition engine
│   ├── llm/               # Local LLM translator
│   ├── pipeline/          # End-to-end orchestration
│   └── tts/               # (Optional placeholder)
│
├── demo/
│   └── sample_audio/      # Test input audio
│
├── docs/                  # Documentation
└── requirements.txt
```

---

## Installation

### 1) Clone Repository

```
git clone https://github.com/avikal07/Ai-Soc.git
cd Ai-Soc
```

### 2) Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3) Install Dependencies

```
pip install -r requirements.txt
```

---

## Download Required Models

Models are not included due to size constraints.

### Speech Recognition Model

```
mkdir -p edge_pipeline/stt/model
cd edge_pipeline/stt/model
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
cd ../../..
```

### LLM Translation Model

```
mkdir -p edge_pipeline/llm/model
cd edge_pipeline/llm/model
wget -O tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf \
https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf
cd ../../..
```

---

## Run the System

```
python -m edge_pipeline.pipeline.realtime_loop
```

---

## Example Output

```
Final Transcription:
hello how are you today i am testing my speech translation project

Translated Text:
Hola, ¿cómo estás hoy? Estoy probando mi proyecto de traducción de voz.
```

---

## Edge AI Design Considerations

This project simulates deployment on ARM edge devices.

Conceptual optimizations:

* Quantized LLM reduces memory footprint
* Streaming inference lowers latency
* CPU-only execution improves portability
* Suitable for NEON vectorization on ARM CPUs
* Compatible with SME2 acceleration on modern ARM cores
* Power-efficient offline processing

---

## Limitations

* Small models reduce translation accuracy
* Semantic translation instead of exact translation
* No real microphone input (WSL limitation)
* Latency higher than cloud systems

---

## Future Work

* Replace WAV simulation with real microphone
* Add multilingual selection
* Implement on-device Text-to-Speech
* ARM hardware benchmarking
* Model distillation for faster inference

---

## Demo Video

(Add your YouTube link here)

---

## Technologies Used

Python, Vosk, TinyLlama, CTransformers, Edge AI, Quantized LLMs

---

## Author

Avikal
