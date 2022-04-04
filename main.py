from time import sleep
from pyfirmata import Arduino
from config import PORT
import sounddevice as sd
import numpy as np
import keyboard

board = Arduino(PORT)

def print_sound(indata, outdata, frames, time, status):
    volume_norm = int((np.linalg.norm(indata) * 10).round())
    if volume_norm < 100:
        val = volume_norm // 10
        if val > 0:
            pin = val + 1
            for i in range(2, pin + 1):
                board.digital[i].write(1)
                sleep(0.03)
            for i in range(2, pin + 1):
                board.digital[i].write(0)
    else:
        print('overflow')

with sd.Stream(callback=print_sound):
    keyboard.wait('q')
