import argparse
import time
import wave

import pyaudio

from fistas.sampler import Sampler


# temporarily reduced keys because it's a pain to record 10
# should be: "w a s d f up down left right space"
KEYS = set("w a s d".split())

CLIP_LENGTH = 2.5
DELAY_BEFORE_RECORDING = 0.1


class Application:
    def __init__(self):
        self.sampler = Sampler(KEYS)

    def run(self, record_mode: bool = False):
        if record_mode:
            self.record()
        else:
            self.sampler.run(record_mode)

    def record(self):
        for key in KEYS:
            self.record_sound(key)

    def record_sound(self, key):
        chunk = 4096  # samples per chunk
        sample_format = pyaudio.paInt16  # bits per sample (ADC val)
        channels = 1  # mono/stereo
        frequency = 22050

        p = pyaudio.PyAudio()

        input(f"Recording {key}, press Enter to start")
        time.sleep(DELAY_BEFORE_RECORDING)

        stream = p.open(
            format=sample_format,
            channels=channels,
            rate=frequency,
            frames_per_buffer=chunk,
            input=True,
        )
        frames = []
        for _ in range(0, int(frequency / chunk * CLIP_LENGTH)):
            data = stream.read(chunk)
            frames.append(data)
        stream.stop_stream()
        stream.close()

        p.terminate()
        print("Finished recording, saving to file...")

        wf = wave.open(key + ".wav", "wb")
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(frequency)
        wf.writeframes(b"".join(frames))
        wf.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--record", action="store_true")
    args = parser.parse_args()

    app = Application()
    app.run(args.record)
