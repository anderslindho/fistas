#!/usr/bin/env python3

import numpy as np
import pygame


def play_sound(key, loop=False):
    filename = key + '.wav'
    sound = pygame.mixer.Sound(filename)
    snd_array = pygame.sndarray.array(sound)
    snd_out = pygame.sndarray.make_sound(snd_array)
    snd_out.play(-1) if loop else snd_out.play()

def main():
    keys = []
    keymods = []
    with open('keys.conf', 'r') as f:
        for line in f:
            keys.append(line.strip())

    screen = pygame.display.set_mode((1, 1))
    pygame.mixer.init(frequency=22050, size=-16, channels=32, buffer=4096)
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if key in keys:
                if key == 'a':
                    play_sound(key, True)
                elif key == 'g':
                    pygame.mixer.quit()
                else: 
                    play_sound(key)
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise KeyboardInterrupt


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Goodbye')
