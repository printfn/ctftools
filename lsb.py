#!/usr/bin/env python3

import math
import os
import wave
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <audio.wav>")
    sys.exit(1)

sound = wave.open(sys.argv[1], 'rb')
channels = sound.getnchannels()
sample_width = sound.getsampwidth()
num_frames = sound.getnframes()
sound_frames = sound.readframes(num_frames)

print(f"channels: {channels}")
print(f"sample_width: {sample_width} bytes")
print(f"num_frames: {num_frames}")
print(f"sound_frames: {len(sound_frames)}")

num = 0
bit_count = 0

for n in [-256, -128, -64, -32, -16, -8, -4, -2, -1, 1, 2, 4, 8, 16, 32, 64, 128, 256]:
    for byte in sound_frames[::n]:
        num = num << 1
        num |= byte & 1
        bit_count += 1
        if bit_count == 8:
            print(chr(num), end="")
            num = 0
            bit_count = 0
