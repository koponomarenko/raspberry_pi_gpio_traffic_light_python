from gpiozero import LED, Button, Buzzer
from time import sleep

# initialize GPIO elements
red_light = LED(25)
yellow_light = LED(8)
green_light = LED(7)
button = Button(2)
buzzer = Buzzer(15)

# set all lights OFF
red_light.off()
yellow_light.off()
green_light.off()

# start the sequence when a button is pressed
print("Press the button to start the traffic light")
button.wait_for_press()

button_pressed = False # keeps button state
def on_button_press():
    global button_pressed
    button_pressed = True
    print("INFO: button press detected")

# set a function to be called when the button is pressed
button.when_pressed = on_button_press

while True:
    if button_pressed == False:
        print("INFO: beginning of the regular sequence")
        red_light.on()
        sleep(5)

        yellow_light.on()
        sleep(2)

        red_light.off()
        yellow_light.off()
        green_light.on()
        sleep(5)

        green_light.off()
        yellow_light.on()
        sleep(5)

        yellow_light.off()
    else:
        print("INFO: allow pedestrian crossing")
        
        red_light.on()
        
        for i in range(0, 10):
            buzzer.on()
            sleep(0.2)
            
            buzzer.off()
            sleep(0.2)
        
        red_light.off()
        button_pressed = False
