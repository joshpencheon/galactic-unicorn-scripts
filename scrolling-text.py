import machine, time
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY

galactic = GalacticUnicorn()
graphics = PicoGraphics(DISPLAY)

message = "Oh how great it is to read in both directions"
speed = 20
background = (  0,   0,   0)
foreground = (  0, 150,  50)
scale = 1
spacing = 1

graphics.set_font("bitmap8")
width = graphics.measure_text(message, scale = scale, spacing = spacing)

x = GalacticUnicorn.WIDTH
y = 2
step = -1
entering = True

while True:
    lower_limit = min(GalacticUnicorn.WIDTH - width, 1)
    if entering:
        upper_limit = GalacticUnicorn.WIDTH + 1
    else:
        upper_limit = max(GalacticUnicorn.WIDTH - width, 1)
    x = min(max(x + step, lower_limit), upper_limit)

    if x == lower_limit or x == upper_limit:
        step *= -1
        entering = False

    graphics.set_pen(graphics.create_pen(*background))
    graphics.clear()

    graphics.set_pen(graphics.create_pen(*foreground))
    graphics.text(message, x, y, wordwrap = -1, scale = scale, spacing = spacing)

    galactic.update(graphics)
    time.sleep(1 / speed)
