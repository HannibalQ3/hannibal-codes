basic.showIcon(IconNames.No)
xgo.init_xgo_serial(SerialPin.P2, SerialPin.P1)
basic.forever(function on_forever() {
    basic.showIcon(IconNames.Heart)
    basic.showIcon(IconNames.SmallHeart, 450)
    basic.clearScreen()
    basic.pause(100)
})
