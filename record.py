#!/usr/bin/env python3

import time
import pyaudio
import wave

def record_sound(key):
    chunk = 1024  # Samples per chunk
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2 # Stereo
    fs = 44100  # Record at 44100 samples per second
    seconds = 3
    filename = key + '.wav'
    frames = []
    
    p = pyaudio.PyAudio()
    print(f'Recording {key}')
    time.sleep(0.3)

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)


    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    print('Finished recording')

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

def main():
    keys = []

    with open('mappings.conf', 'r') as f:
        for line in f:
            keys.append(line.strip())

    for key in keys:
        record_sound(key)


if __name__ == '__main__':
    main()
