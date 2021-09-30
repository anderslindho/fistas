import argparse
from abc import abstractmethod
import time
import wave

import pyaudio

from fistas.sampler import Sampler


# temporarily reduced keys because it's a pain to record 10
# should be: "w a s d f up down left right space"
KEYS = set("w a s d".split())

DELAY_BEFORE_RECORDING = 0.1


class OStream:
    chunk = 1024

    def __init__(self, filename, modify = 1):
        self.ctx = pyaudio.PyAudio()
        self.wf = wave.open(filename, 'rb')
        self.stream = self.ctx.open(
            format = self.ctx.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = int(modify * self.wf.getframerate()),
            output = True,
        )

    def write(self):
        while True:
            data = self.wf.readframes(self.chunk)
            if not data:
                break
            self.stream.write(data)

    def close(self):
        self.stream.close()
        self.ctx.terminate()

class IStream:
    chunk = 4096
    sample_format = pyaudio.paInt16
    channels = 1
    frequency = 22050

    def __init__(self, filename, length = 2):
        self.length = length
        self.ctx = pyaudio.PyAudio()
        self.wf = wave.open(filename, 'wb')
        self.wf.setnchannels(self.channels)
        self.wf.setsampwidth(self.ctx.get_sample_size(self.sample_format))
        self.wf.setframerate(self.frequency)
        self.stream = self.ctx.open(
            format=self.sample_format,
            channels=self.channels,
            rate=self.frequency,
            frames_per_buffer=self.chunk,
            input=True,
        )

    def write(self):
        frames = []
        for _ in range(0, int(self.frequency / self.chunk * self.length)):
            data = self.stream.read(self.chunk)
            frames.append(data)
        self.stream.stop_stream()
        self.wf.writeframes(b"".join(frames))

    def close(self):
        self.stream.close()
        self.ctx.terminate()


import threading

class Application:
    def __init__(self):
        pass

    def run(self):
        self.record_sound("d")
        self.play_sound("d")
        time.sleep(0.5)
        for i in range(10):
            threading.Thread(target=self.play_sound, args=('d', 1.5 - i * 0.1), daemon=False).start()
            time.sleep(0.1)
        #self.play_sound("d", 0.6)
        #self.play_sound("d", 1.2)

    def play_sound(self, key, modify = 1):
        oas = OStream(f"{key}.wav", modify)
        oas.write()
        oas.close()

    def record_sound(self, key):
        ias = IStream(f"{key}.wav")
        ias.write()
        ias.close()


def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    app = Application()
    app.run()
