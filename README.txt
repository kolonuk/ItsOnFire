ItsOnFire!
A simple web interface and API to trigger a warning. Code taken from https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/

Use case:

* Have zabbix call a web trigger when an alert is required.
* The main purpose in this case is to make a warning beacon flash when there is an issue in zabbix, but you can plug anything that is 3v capable.

Installation
* Install python (https://www.python.org/downloads/windows/)
* Add path to system path
* Install pip (https://www.activestate.com/resources/quick-reads/how-to-install-pip-on-windows/)
* Add path to system path
* Install VSCode
* Install Micropython IDE extension by Bao Phan (https://marketplace.visualstudio.com/items?itemName=dphans.micropython-ide-vscode) (Search Micropython in VSCode)

You can skip this if you alreayd have MicroPython flashed on the device
* Buy a ESP3266 or ESP32 (https://www.google.com/search?q=buy+esp3266)
  * Untested, but it might even work with the new Raspberry Pi Pico w!
* Flash with Micropython (https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html)

Flash/Setup
* Download this project (git clone https://www.github.com/kolonuk/ItsOnFire)
* Copy the wifi.example.py file and rename it to wifi.py. Edit to match your Wifi.
* Attach something to pin 2 - an LED, relay, etc.
* Apply power!

* You now have a smart whatever!

For on-the-go programming, you can use Thonny - it has capability to do programming directly on the ESP.
