from machine import Pin, Timer
import time

# Define GPIO pins
I_pin = Pin(1, Pin.IN, Pin.PULL_UP)  # D (Data) input, with internal pull-up resistor
O_pin = Pin(4, Pin.OUT)  # Q (Output) pin

# State variables
last_I_value = 0  # Initial value of D (assuming pull-up resistor on D_pin)
Q_value = 0  # Initial value of Q
counter = 0
current_I_value =0
TimerCount = 0
speed = 0
machine.freq(200_000_000)
# Main loop
while True:
    current_I_value = I_pin.value()
    
    if current_I_value  != last_I_value:  # This is the edge detection logic
        counter = counter + 1
         
    TimerCount = TimerCount + 1
    # Store current D value for the next cycle to detect edge change
    last_I_value = current_I_value
    if TimerCount == 100:
        speed = (1/36) * counter * 5.65487 * 2
        print("Speed:", speed, " cm/s")
        TimerCount = 0
        counter = 0
    time.sleep(0.01)  # Keep the main loop running while the timer triggers the flip-flop
    
