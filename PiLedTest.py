
from time import sleep
from src.hal import hal_input_switch as switch
from src.hal import hal_led as led

def main():
    switch.init()
    led.init()
    while True:
        ReadSwitch = switch.read_slide_switch()
        # check the current position of the switch
        if ReadSwitch == 0 :
            for i in range(0,25):
                led.set_output(1, 1)
                sleep(0.1)
                led.set_output(1, 0)
                sleep(0.1)
            while ReadSwitch == 0:
                ReadSwitch = switch.read_slide_switch()
                sleep(0.1)
        else:
            led.set_output(1, 0)
if __name__ == "__main__":
    main()





