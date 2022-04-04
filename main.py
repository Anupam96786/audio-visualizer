from pyfirmata import Arduino
from config import PORT
import sounddevice as sd
import numpy as np
import keyboard

board = Arduino(PORT)
prev_val = 1

def print_sound(indata, outdata, frames, time, status):
    global prev_val
    volume_norm = int((np.linalg.norm(indata) * 10).round())
    if volume_norm < 100:
        val = volume_norm // 10
        if val > 0:
            if prev_val < val:
                for i in range(prev_val, val + 1):
                    pin = i + 1
                    board.digital[pin].write(1)
            elif prev_val > val:
                for i in range(prev_val + 1, val, -1):
                    pin = i + 1
                    board.digital[pin].write(0)
            prev_val = val

with sd.Stream(callback=print_sound):
    keyboard.wait('q')
