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
    keys = []
    keymods = []
    sounds = {}
    with open('keys.conf', 'r') as f:
        for line in f:
            keys.append(line.strip())

    pygame.mixer.init(frequency=22050, size=-16, channels=32, buffer=500)
    for key in keys:
        create_sound(key, sounds)

    screen = pygame.display.set_mode((1, 1))
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
                sounds[key].fadeout(50)
                is_playing[key] = False


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Goodbye')
