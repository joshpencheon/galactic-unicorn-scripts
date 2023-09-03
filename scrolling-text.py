import machine, time
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY

galactic = GalacticUnicorn()
graphics = PicoGraphics(DISPLAY)

message = "Hi from Josh!"
speed = 20
background = (  0,   0,   0)
foreground = (  0, 250,   0)
scale = 1
spacing = 1

graphics.set_font("bitmap8")
width = graphics.measure_text(message, scale, spacing)

x = GalacticUnicorn.WIDTH
y = 2

while True:
    x = max(x - 1, GalacticUnicorn.WIDTH - width)

    graphics.set_pen(graphics.create_pen(*background))
    graphics.clear()

    graphics.set_pen(graphics.create_pen(*foreground))
    graphics.text(message, x, y, -1, scale, spacing)

    galactic.update(graphics)
    time.sleep(1 / speed)
