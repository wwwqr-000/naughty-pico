# naughty-pico
Raspberry pi pico, but a rubberducky (can execute payload from pico's own storage)

<p>Steps to make it work</p>
<li>Download rubberducky generator.exe and execute it</li>
<li>Choose a location where the files should be placed. (Location doesn't matter)</li>
<li>Connect Raspberry pi pico to windows mashine using USB</li>
<li>Drop reset.uf2 into the root directory of the pico</li>
<li>Wait for the pico to reconnect</li>
<li>Now drop the CIRCUITPY.uf2 into the root directory of the pico</li>
<li>Wait for the pico to reconnect</li>
<li>Move the "adafruit_hid" folder to the root directory of the pico</li>
<li>Place the code.py file from this repo in the root directory of the pico</li>
