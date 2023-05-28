xgo.init_xgo_serial(SerialPin.P2, SerialPin.P1)
basic.show_icon(IconNames.HEART)

def on_forever():
    pass
basic.forever(on_forever)
