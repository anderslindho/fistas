#!/usr/bin/env python3

from argparse import ArgumentParser
import time
import wave

import pyaudio


def recorder(key, length):
    for key in keys:
        record_sound(key, length)


def record_sound(key, length):
    chunk = 4096  # samples per chunk
    sample_format = pyaudio.paInt16  # bits per sample (ADC val)
    channels = 1 # mono/stereo
    freq = 22050  # samples per second
    filename = key + '.wav'
    frames = []
    delay = 0.1 # seconds

    p = pyaudio.PyAudio()
    input(f'Recording {key}, press Enter to start')
    time.sleep(delay)
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=freq,
                    frames_per_buffer=chunk,
                    input=True)
    for i in range(0, int(freq / chunk * length)):
        data = stream.read(chunk)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    print('Finished recording, saving to file...')

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(freq)
    wf.writeframes(b''.join(frames))
    wf.close()


def main():
    parser = ArgumentParser()
    parser.add_argument("key")
    parser.add_argument("-l", "--length", type=int)

    args = parser.parse_args()

    record_sound(**vars(args))


if __name__ == "__main__":
    main()
