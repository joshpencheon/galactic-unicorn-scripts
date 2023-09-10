import time
import random
import _thread

from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY

cols = GalacticUnicorn.WIDTH
rows = GalacticUnicorn.HEIGHT

dots = [ [False]*rows for _ in range(cols) ]

lock = _thread.allocate_lock()

def render():
    global lock, dots

    galactic = GalacticUnicorn()
    graphics = PicoGraphics(DISPLAY)

    background = (  0,   0,   0)
    foreground = (  0, 150,   0)

    fps = 30

    while True:
        graphics.set_pen(graphics.create_pen(*background))
        graphics.clear()
        graphics.set_pen(graphics.create_pen(*foreground))

        lock.acquire()

        for x in range(len(dots)):
            for y in range(len(dots[x])):
                if dots[x][y]:
                    graphics.pixel(x, y)

        lock.release()
        galactic.update(graphics)
        time.sleep(1 / fps)

def generate_dots():
    global lock, dots

    rate = 100

    while True:
        lock.acquire()

        x = random.randint(0, len(dots) - 1)
        y = random.randint(0, len(dots[x]) - 1)
        dots[x][y] = not(dots[x][y])

        lock.release()

        time.sleep(1 / rate)

# Push rendering onto the other core:
_thread.start_new_thread(render, ())

# Mutate the data on a loop on the primary core:
generate_dots()
