import pygame


class Sampler:
    def __init__(self, keys: list):
        self.keys = keys
        self.fade_time_ms = 100
        self.frequency = 22050
        self.sample_size = -16  # bits
        self.channels = 32
        self.block_size = 256

        self.sounds = {}

    def run(self):
        pygame.mixer.init(
            frequency=self.frequency,
            size=self.sample_size,
            channels=self.channels,
            buffer=self.block_size,
        )
        for key in self.keys:
            self.create_sound(key)

        screen = pygame.display.set_mode(size=(480, 360))
        screen.fill([60, 140, 180])
        pygame.display.set_caption("Fistas")
        pygame.display.flip()

        is_playing = {k: False for k in self.keys}

        while True:
            event = pygame.event.wait()
            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                key = pygame.key.name(event.key)
                if event.type == pygame.KEYDOWN:
                    if key in self.keys:
                        self.play_sound(key, True)
                        is_playing[key] = True
                    elif event.key == pygame.K_ESCAPE:
                        break
                elif event.type == pygame.KEYUP and key in self.keys:
                    self.sounds[key].fadeout(self.fade_time_ms)
                    is_playing[key] = False

        pygame.quit()

    def create_sound(self, key):
        filename = key + ".wav"
        self.sounds[key] = pygame.mixer.Sound(filename)

    def play_sound(self, key, loop=False):
        if loop:
            self.sounds[key].play(-1)
        else:
            self.sounds[key].play()
