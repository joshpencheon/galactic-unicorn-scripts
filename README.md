# Galactic Unicorn scripts

A selection of scripts to play with on Pimoroni's [Galactic Unicorn](https://shop.pimoroni.com/products/space-unicorns?variant=40842033561683) Pico W-powered LED matrix.

## Getting started

```bash
# Install mpremote, for contacting the Pico W over serial bus
pip3 install mpremote

# Run an example:
mpremote run scrolling-text.py
```

## Wi-Fi connectivity

In order to connect to the network, the Pico W will need an SSID and password. Create these in a standalone file:

```python
# secrets.py
SSID = "my-network"
PASSWORD = "my-passphrase"
```

Then, copy the file over to the Pico W:

```bash
mpremote fs cp secrets.py :secrets.py
```

To test everything is working, run the example:

```bash
mpremote run wlan_connectivity.py
```
