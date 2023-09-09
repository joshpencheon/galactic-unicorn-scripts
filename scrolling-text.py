import machine, time
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY

galactic = GalacticUnicorn()
graphics = PicoGraphics(DISPLAY)

message = "Hi from Josh!"
speed = 20
background = (  0,   0,   0)
foreground = (  0, 150,  50)
scale = 1
spacing = 1

graphics.set_font("bitmap8")
width = graphics.measure_text(message, scale = scale, spacing = spacing)

x = GalacticUnicorn.WIDTH
y = 2

while True:
    x = max(x - 1, min(GalacticUnicorn.WIDTH - width, 1))

    graphics.set_pen(graphics.create_pen(*background))
    graphics.clear()

    graphics.set_pen(graphics.create_pen(*foreground))
    graphics.text(message, x, y, wordwrap = -1, scale = scale, spacing = spacing)

    galactic.update(graphics)
    time.sleep(1 / speed)
