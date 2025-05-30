# naughty-pico
Raspberry pi pico, but a rubberducky (can execute payload from pico's own storage)

<p>Steps to make it work:</p>
<li>Connect Raspberry pi pico (while holding the BOOTSEL button) to windows mashine using USB</li>
<li>Drop reset.uf2 into the root directory of the pico</li>
<li>Wait for the pico to reconnect</li>
<li>Now drop the CIRCUITPY.uf2 into the root directory of the pico</li>
<li>Wait for the pico to reconnect</li>
<li>Download <code>naughty-pico-installer.exe</code> When promted, select root directory of pico, for example: <code>D:\</code></li>
<li>Install 7z (if you don't have it already)</li>
<li>Execute <code>attrib +h +s * /d</code> in the root directory of the pico (cmd)</li>
<li>Reconnect the pico</li>
<li>With 7z open the root directory of the pico, for example: <code>D:\</code> as path</li>
<li>Edit naughty-pico\payload.cmd to your likings (bottom command ejects the pico from the connected device and erases WIN + R buffer)</li>
<li>Edit code.py to your likings. To enable and disable the naughty-pico, change trigger to True or False (bottom of code.py)</li>

<h2>Nice to know</h2>
<li>It will start immediately, to edit the payload.cmd or code.py, do: WIN + L to goto the lock screen, then wait for the pico to finish, then login and change <code>trigger(True)</code> to <code>trigger(False)</code> in code.py</li>
<li>Use <code>%~d0</code> in payload.cmd to use as disk variable. Example: %~d0 is the drive letter of the disk payload.cmd is executed from in this format: LETTER:\</li>
