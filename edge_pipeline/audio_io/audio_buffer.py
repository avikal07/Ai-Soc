import queue


class AudioBuffer:
    """
    Thread-safe buffer for streaming audio chunks.
    Implements producer-consumer separation.
    """

    def __init__(self, max_chunks=50):
        self.buffer = queue.Queue(maxsize=max_chunks)

    def write(self, chunk):
        if not self.buffer.full():
            self.buffer.put(chunk)

    def read(self):
        if not self.buffer.empty():
            return self.buffer.get()
        return None
