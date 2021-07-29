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
time.sleep(1)
device.emit(uinput.REL_X,screen_width)
device.emit(uinput.REL_Y,screen_height)

import webbrowser
webbrowser.open_new_tab("https://www.thebluebook.com")