from galactic import GalacticUnicorn
import time

buttons = {
    "a": GalacticUnicorn.SWITCH_A,
    "b": GalacticUnicorn.SWITCH_B,
    "c": GalacticUnicorn.SWITCH_C,
    "d": GalacticUnicorn.SWITCH_D,
    "zzz": GalacticUnicorn.SWITCH_SLEEP,
    "v+": GalacticUnicorn.SWITCH_VOLUME_UP,
    "v-": GalacticUnicorn.SWITCH_VOLUME_DOWN,
    "b+": GalacticUnicorn.SWITCH_BRIGHTNESS_UP,
    "b-": GalacticUnicorn.SWITCH_BRIGHTNESS_DOWN
}

states = dict((name, False) for name in buttons)
gu = GalacticUnicorn()

while True:
    events = []

    for name, pin in buttons.items():
        is_pressed = gu.is_pressed(pin)
        was_pressed = states[name]
        states[name] = is_pressed

        if is_pressed != was_pressed:
            action = "pressed" if is_pressed else "released"
            events.append(f"Button {name} was {action}")

    for event in events:
        print(event)

    time.sleep(0.001)
