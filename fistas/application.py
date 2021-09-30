from pathlib import Path
import sys
from PySide2.QtGui import QWindow

from PySide2.QtWidgets import QApplication, QHBoxLayout, QLabel, QVBoxLayout, QWidget, QFileDialog, QMainWindow
from PySide2.QtMultimedia import QSound
from PySide2.QtCore import Qt, Slot



import logging
logging.basicConfig(level=logging.DEBUG)


class Sampler:
    keymap = {
        Qt.Key_A: "a",
        Qt.Key_W: "w",
        Qt.Key_S: "s",
        Qt.Key_D: "d",
        Qt.Key_F: "f",
        Qt.Key_Space: " ",
        Qt.Key_Left: "left",
        Qt.Key_Right: "right",
        Qt.Key_Up: "up",
        Qt.Key_Down: "down",
        Qt.Key_Enter: "enter",
    }

    def __init__(self):
        self.sounds = {}

    def load_sound(self, path, key):
        logging.debug(f"loading {path=} to {key=}")
        sound = QSound(str(path))
        self.sounds[key] = sound

    def play(self, key):
        try:
            self.sounds[self.keymap[key]].play()
        except KeyError:
            return

    def silence(self, key):
        try:
            self.sounds[self.keymap[key]].stop()
        except KeyError:
            return
        else:
            logging.debug(f"muting {key=}")

    def loop(self, key):
        try:
            self.sounds[self.keymap[key]].setLoops(-1)
        except KeyError:
            return
        else:
            logging.debug(f"looping {key=}")


class MainWindow(QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        QWidget.__init__(self, parent, *args, **kwargs)
        self.setWindowTitle("fistas")

        self.sampler = Sampler()

        self.sampler.load_sound("space.wav", "w")
        self.sampler.load_sound("s.wav", "a")

    def keyPressEvent(self, event):
        if (event.modifiers() & Qt.ShiftModifier):
            self.sampler.loop(event.key())
        elif (event.modifiers() & Qt.ControlModifier):
            self.sampler.silence(event.key())
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
