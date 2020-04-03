
# how you flash it:

esptool.py --port /dev/cu.SLAB_USBtoUART erase_flash
esptool.py --port /dev/cu.SLAB_USBtoUART  --baud 460800 write_flash --flash_size=detect 0 esp8266-20190529-v1.11.bin


# how you screen in from OSX:
screen /dev/cu.SLAB_USBtoUART 115200,cs8,-parenb,-cstopb,echo


# set the network
import network
wlan = network.WLAN(network.STA_IF)
wlan.ifconfig()
wlan.active(True)
wlan.connect('macallister', '6175525152')
# or:
wlan.connect('Matrix', 'MatrixWaltham')


wlan.active(True)
wlan.scan() 
wlan.isconnected()

wlan.ifconfig()


# for webrepl:

import webrepl_setup


from machine import Pin

import ntptime
from machine import RTC
ntptime.settime()
rtc = RTC()
rtc.datetime()

# 4PM ET is 9PM UTC
# 8PM ET is 1AM UTC

def http_get(url):
    import socket
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()