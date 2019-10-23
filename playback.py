#!/usr/bin/env python3

import time
import numpy as np
import pygame

def create_sound(key, sounds):
    filename = key + '.wav'
    sound = pygame.mixer.Sound(filename)
    sounds[key] = sound

def play_sound(key, sounds, loop=False):
    sounds[key].play(-1) if loop else sounds[key].play()

def main():
    fade_time = 100 # ms
    freq = 22050 # Hz
    size = -16 # bits
    channels = 32
    block = 256 # buffer size

    keys = []
    sounds = {}
    with open('keys.conf', 'r') as f:
        for line in f:
            keys.append(line.strip())

    pygame.mixer.init(frequency=freq, size=size, channels=channels, buffer=block)
    for key in keys:
        create_sound(key, sounds)
        time.sleep(0.1)

    screen = pygame.display.set_mode(size=(480, 360))
    screen.fill([60, 180, 140])
    pygame.display.set_caption('Fistas')
    pygame.display.flip()

    is_playing = {k: False for k in keys}
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:    
            key = pygame.key.name(event.key)
            if key in keys:
                if key == 'f':
                    pygame.mixer.stop()
                elif key in ('w', 'a'):
                    play_sound(key, sounds, True)
                else:
                    play_sound(key, sounds)
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise KeyboardInterrupt


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Goodbye')
