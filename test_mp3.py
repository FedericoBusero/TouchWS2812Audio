# SPDX-FileCopyrightText: 2020 Jeff Epler for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Audio Out MP3 Example"""
from config import audio_output 
import digitalio
from audiomp3 import MP3Decoder

# The listed mp3files will be played in order
mp3files = ["tardis.mp3"]

# You have to specify some mp3 file when creating the decoder
mp3 = open(mp3files[0], "rb")
decoder = MP3Decoder(mp3)

while True:
    for filename in mp3files:
        # Updating the .file property of the existing decoder
        # helps avoid running out of memory (MemoryError exception)
        decoder.file = open(filename, "rb")
        audio_output.play(decoder)
        print("playing", filename)

        # This allows you to do other things while the audio plays!
        while audio_output.playing:
            pass

        print("next song")
