let Distance_To_Object = 0
basic.showIcon(IconNames.Yes)
basic.pause(500)
basic.forever(function on_forever() {
    
    Distance_To_Object = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.Centimeters)
    basic.showNumber(Distance_To_Object)
})
