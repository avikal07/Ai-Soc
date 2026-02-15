import wave
import time


class WavStream:
    """
    Simulates real-time microphone streaming using a WAV file.
    """

    def __init__(self, wav_path, chunk_size=1024, realtime=True):
        self.wav = wave.open(wav_path, 'rb')
        self.chunk_size = chunk_size
        self.realtime = realtime
        self.rate = self.wav.getframerate()

    def read_chunk(self):
        data = self.wav.readframes(self.chunk_size)

        if self.realtime and data:
            time.sleep(self.chunk_size / self.rate)

        return data

    def close(self):
        self.wav.close()
