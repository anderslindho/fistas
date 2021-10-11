from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtMultimedia import QSound
from PySide2.QtCore import Qt



import logging
#logging.basicConfig(level=logging.WARNING)


class Sampler:
    def __init__(self):
        self.sounds = {}

    def load_sound(self, path, key):
        logging.debug(f"loading {path=} to {key=}")
        sound = QSound(str(path))
        self.sounds[key] = sound

    def play(self, key):
        try:
            self.sounds[key].play()
        except KeyError:
            return
        else:
            logging.debug(f"playing {key=}")

    def silence(self, key):
        try:
            self.sounds[key].stop()
        except KeyError:
            return
        else:
            logging.debug(f"muting {key=}")

    def loop(self, key):
        try:
            self.sounds[key].setLoops(-1)
        except KeyError:
            return
        else:
            logging.debug(f"looping {key=}")


class MainWindow(QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        QWidget.__init__(self, parent, *args, **kwargs)
        self.setWindowTitle("fistas")

        self.sampler = Sampler()

        # possible keys:
        # Qt.Key_A,
        # Qt.Key_W,
        # Qt.Key_S,
        # Qt.Key_D,
        # Qt.Key_F,
        # Qt.Key_Space,
        # Qt.Key_Left,
        # Qt.Key_Right,
        # Qt.Key_Up,
        # Qt.Key_Down,
        # Qt.Key_Enter,

        self.sampler.load_sound("rhythm.wav", Qt.Key_W)
        self.sampler.load_sound("say.wav", Qt.Key_A)
        self.sampler.load_sound("thing.wav", Qt.Key_S)
        self.sampler.load_sound("blupp.wav", Qt.Key_D)
        self.sampler.load_sound("bass.wav", Qt.Key_Up)
        self.sampler.load_sound("bass.wav", Qt.Key_Down)
        self.sampler.load_sound("hihat.wav", Qt.Key_Left)
        self.sampler.load_sound("test.wav.wav", Qt.Key_Right)

    def keyPressEvent(self, event):
        if (event.modifiers() & Qt.ShiftModifier):
            self.sampler.loop(event.key())
        elif (event.modifiers() & Qt.ControlModifier):
            self.sampler.silence(event.key())
        elif (event.modifiers() & Qt.AltModifier):
            pass
        elif (event.modifiers() & Qt.MetaModifier):
            pass
        else:
            self.sampler.play(event.key())

    def keyReleaseEvent(self, event):
        pass


def main():
    import sys

    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(400, 300)
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
