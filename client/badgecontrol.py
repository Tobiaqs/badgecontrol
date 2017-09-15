import ugfx, appglue, wifi, usocket, badge, time

badge.nvs_set_str("badge", "wifi.ssid", "hi")
badge.nvs_set_str("badge", "wifi.password", "hellohello")

font = "Roboto_Regular12"

ugfx.init()
ugfx.input_init()
ugfx.input_attach(ugfx.BTN_START, lambda pressed: appglue.home() if pressed else None)

wifi.init()

ugfx.clear(ugfx.BLACK)
ugfx.string(50, 25, "STILL", "Roboto_BlackItalic24", ugfx.WHITE)
ugfx.string(30, 50, "Connecting to wifi", "PermanentMarker22", ugfx.WHITE)
le = ugfx.get_string_width("Connecting to wifi", "PermanentMarker22")
ugfx.line(30, 72, 30 + 14 + le, 72, ugfx.WHITE)
ugfx.string(140, 75, "Anyway", "Roboto_BlackItalic24", ugfx.WHITE)
ugfx.flush()

#slower than default to save energy
while not wifi.sta_if.isconnected():
  time.sleep(0.5)

ugfx.clear(ugfx.WHITE)
ugfx.flush()
ugfx.clear(ugfx.BLACK)
ugfx.flush()
ugfx.clear(ugfx.WHITE)
ugfx.string_box(0, 0, 296, 128, "My IP: " + wifi.sta_if.ifconfig()[0] + "\nLet me know your IP", font, ugfx.BLACK, ugfx.justifyCenter)
ugfx.flush()

s = usocket.socket()
ai = usocket.getaddrinfo("0.0.0.0", 80)
addr = ai[0][-1]
s.bind(addr)
s.listen(5)

ip = s.accept()[1]

s.close()

s = usocket.socket()
addr = usocket.getaddrinfo(ip, 1337)[0][-1]
s.connect(addr)


ugfx.clear(ugfx.BLACK)
ugfx.flush()
ugfx.clear(ugfx.WHITE)
ugfx.string_box(0, 0, 296, 128, "My IP: " + wifi.sta_if.ifconfig()[0] + "\nYour IP: " + ip, font, ugfx.BLACK, ugfx.justifyCenter)
ugfx.flush()

def send(action):
  s.send(action)

ugfx.input_attach(ugfx.JOY_LEFT, lambda pressed: send("left") if pressed else None)
ugfx.input_attach(ugfx.JOY_UP, lambda pressed: send("up") if pressed else None)
ugfx.input_attach(ugfx.JOY_RIGHT, lambda pressed: send("right") if pressed else None)
ugfx.input_attach(ugfx.JOY_DOWN, lambda pressed: send("down") if pressed else None)
ugfx.input_attach(ugfx.BTN_A, lambda pressed: send("A") if pressed else None)
ugfx.input_attach(ugfx.BTN_B, lambda pressed: send("B") if pressed else None)
ugfx.input_attach(ugfx.BTN_SELECT, lambda pressed: send("SELECT") if pressed else None)