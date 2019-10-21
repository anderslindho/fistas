#!/usr/bin/env python3

import numpy as np
import time
import pyaudio
import wave
import pygame

def play_sound(key, p):
    filename = key + '.wav'
    wf = wave.open(filename, 'r')
    
    def callback(in_data, frame_count, time_info, flag):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True,
                    stream_callback=callback)

    stream.start_stream()
    while stream.is_active():
        time.sleep(0.1)

    stream.stop_stream()
    stream.close()

def main():
    keys = []
    p = pyaudio.PyAudio()

    with open('mappings.conf', 'r') as f:
        for line in f:
            keys.append(line.strip())

    screen = pygame.display.set_mode((500, 500))

    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            print(key)

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                p.terminate()
                raise KeyboardInterrupt
            elif key in keys:
                play_sound(key, p)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Goodbye')
