#!/usr/bin/env python3

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

    screen = pygame.display.set_mode(size=(480, 360))
    screen.fill([60, 140, 180])
    pygame.display.set_caption('Fistas')
    pygame.display.flip()

    is_playing = {k: False for k in keys}
    while True:
        event = pygame.event.wait()
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            key = pygame.key.name(event.key)
            if event.type == pygame.KEYDOWN:    
                if key in keys:
                    play_sound(key, sounds, True)
                    is_playing[key] = True
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    raise KeyboardInterrupt
            elif event.type == pygame.KEYUP and key in keys:
                sounds[key].fadeout(fade_time)
                is_playing[key] = False


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Goodbye')
