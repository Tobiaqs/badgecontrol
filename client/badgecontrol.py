import ugfx, appglue, wifi, usocket, badge, time

font = "Roboto_Regular12"

def reset():
	ugfx.input_init()
	ugfx.input_attach(ugfx.BTN_START, lambda pressed: appglue.home() if pressed else None)
	ugfx.input_attach(ugfx.BTN_A, lambda pressed: bind_to_client() if pressed else None)

	ugfx.clear(ugfx.BLACK)
	ugfx.flush()
	ugfx.clear(ugfx.WHITE)
	ugfx.string_box(0, 0, 296, 128, "Press START again to exit.\nPress A to reconnect", font, ugfx.BLACK, ugfx.justifyCenter)
	ugfx.flush()

def bind_to_client():
	ugfx.clear(ugfx.BLACK)
	ugfx.flush()
	ugfx.clear(ugfx.WHITE)
	ugfx.string_box(0, 0, 296, 128, "My IP: " + wifi.sta_if.ifconfig()[0] + "\nReady to receive connection", font, ugfx.BLACK, ugfx.justifyCenter)
	ugfx.flush()

	connection, client_address = socket.accept()

	ugfx.clear(ugfx.BLACK)
	ugfx.flush()
	ugfx.clear(ugfx.WHITE)
	ugfx.string_box(0, 0, 296, 128, "My IP: " + wifi.sta_if.ifconfig()[0] + "\nYour IP: " + client_address[0] +"\nConnection successful\nPress START to disconnect", font, ugfx.BLACK, ugfx.justifyCenter)
	ugfx.flush()

	ugfx.input_init()
	ugfx.input_attach(ugfx.BTN_START, lambda pressed: reset() if pressed else None)
	ugfx.input_attach(ugfx.JOY_LEFT, lambda pressed: connection.sendall(b"left") if pressed else None)
	ugfx.input_attach(ugfx.JOY_UP, lambda pressed: connection.sendall(b"up") if pressed else None)
	ugfx.input_attach(ugfx.JOY_RIGHT, lambda pressed: connection.sendall(b"right") if pressed else None)
	ugfx.input_attach(ugfx.JOY_DOWN, lambda pressed: connection.sendall(b"down") if pressed else None)
	ugfx.input_attach(ugfx.BTN_A, lambda pressed: connection.sendall(b"A") if pressed else None)
	ugfx.input_attach(ugfx.BTN_B, lambda pressed: connection.sendall(b"B") if pressed else None)
	ugfx.input_attach(ugfx.BTN_SELECT, lambda pressed: connection.sendall(b"SELECT") if pressed else None)

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

socket = usocket.socket()
socket.bind(('0.0.0.0', 1337))
socket.listen(1000)

ugfx.clear(ugfx.WHITE)
ugfx.flush()

bind_to_client()