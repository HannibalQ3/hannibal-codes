basic.show_icon(IconNames.NO)
xgo.init_xgo_serial(SerialPin.P2, SerialPin.P1)

def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.show_icon(IconNames.SMALL_HEART, 450)
    basic.clear_screen()
    basic.pause(100)
basic.forever(on_forever)
