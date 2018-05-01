import envirophat
import time
import unicornhat as unicorn

unicorn.set_layout(unicorn.PHAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
envirophat.leds.on()

while True:
    try:
        color = (envirophat.light.rgb())
        for y in range(4):
            for x in range(8):
                r = 128
                g = 0
                b = 0
                unicorn.set_pixel(x,y,(color))
        unicorn.show()
        time.sleep(0.1)
    except KeyboardInterrupt:
        print("EXIT")
        envirophat.leds.off()
        break
