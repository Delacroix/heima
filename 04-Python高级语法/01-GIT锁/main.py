from ctypes import *
from threading import Thread


lib = cdll.LoadLibrary("./libdead_loop.so")

t = Thread(target=lib.DeadLoop)

t.start()

while True:
    pass
