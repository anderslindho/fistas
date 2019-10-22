#!/usr/bin/env python3

import numpy as np
import pygame

def play_sound(key):
    pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=4096)
    filename = key + '.wav'
    sound = pygame.mixer.Sound(filename)
    snd_array = pygame.sndarray.array(sound)
    snd_out = pygame.sndarray.make_sound(snd_array)
    snd_out.play()

def main():
    keys = []
    with open('mappings.conf', 'r') as f:
        for line in f:
            keys.append(line.strip())

    screen = pygame.display.set_mode((1, 1))
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise KeyboardInterrupt
            elif key in keys:
                play_sound(key)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Goodbye')
