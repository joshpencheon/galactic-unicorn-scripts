import network
import time
import secrets
import urequests
import ure

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed, status=' + str(wlan.status()))
else:
    status = wlan.ifconfig()
    print('Connected, IP: ' + status[0])

r = urequests.get('http://example.com')
match = ure.search('<p>(.*?)</p>', r.content.decode())
print("From example.com:")
print(match.group(1))
r.close()
