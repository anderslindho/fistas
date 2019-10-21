#!/usr/bin/env python3


import pyaudio
import wave
import pygame

def play_sound(key):
    filename = key + '.wav'
    chunk = 1024  # Set chunk size of 1024 samples per data frame
    wf = wave.open(filename, 'rb') # Open the sound file 
    p = pyaudio.PyAudio()

    # Open a .Stream object to write the WAV file to
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True)

    data = wf.readframes(chunk) # Read data in chunks

    # Play the sound by writing the audio data to the stream
    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)

    stream.close()
    p.terminate()

def main():
    play_sound('K_a')

main()
