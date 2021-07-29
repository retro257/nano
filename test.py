import uinput
import time


screen_width = 100
screen_height = 100



device = uinput.Device([
         uinput.BTN_LEFT,
         uinput.BTN_RIGHT,
         uinput.REL_X,
         uinput.REL_Y,
         ])
def main():
    time.sleep(1)
    device.emit(uinput.REL_X, -1 * screen_width)
    device.emit(uinput.REL_Y, -1 * screen_height)
if __name__ == '__main__':
    main()