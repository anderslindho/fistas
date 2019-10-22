#!/usr/bin/env python3

import time
import pyaudio
import wave

def record_sound(key):
    chunk = 4096  # samples per chunk
    sample_format = pyaudio.paInt16  # bits per sample (ADC val)
    channels = 1 # mono/stereo
    freq = 22050  # samples per second
    clip_length = 3 # seconds
    filename = key + '.wav'
    frames = []
    
    p = pyaudio.PyAudio()
    print(f'Recording {key}')
    time.sleep(0.3)
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=freq,
                    frames_per_buffer=chunk,
                    input=True)
    for i in range(0, int(freq / chunk * clip_length)):
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
    keys = []
    with open('keys.conf', 'r') as f:
        for line in f:
            keys.append(line.strip())

    print(f'Will record {len(keys)} keys')
    for key in keys:
        record_sound(key)


if __name__ == '__main__':
    main()
