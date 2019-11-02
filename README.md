# Fistas
Made for hobby project with Makey-Makey.
Two small scripts and a config file for available keys.

### record 
Records a 3 sec long wav for each key in mappings.conf
args: keys that you want to record (e.g. use like `./record w a s d`)
if no args it will scan all keys in keys.conf

### playback
Listens for keypresses and plays associated audio

### keys.conf
Valid keys (for scan-record and for playback)

# Prereqs
- pyaudio
- pygame
- numpy
