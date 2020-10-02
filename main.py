Distance_To_Object = 0
basic.show_icon(IconNames.YES)
basic.pause(500)

def on_forever():
    global Distance_To_Object
    Distance_To_Object = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.CENTIMETERS)
    basic.show_number(Distance_To_Object)
basic.forever(on_forever)
