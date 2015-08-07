# occupi


Is the bathroom vacant? Find out by using a Raspberry Pi's GPIO to keep track of if the door is closed*, and display it on a web page.

*\* Adapt to some other on/off state application by attaching a different type of switch.*


## Raspberry Pi setup

The Raspberry Pi is used as a switch state server, but it could also be used to serve the client web app too.


### Hardware

Hook up the switch between the ground pin and GPIO pin `18` (BCM numbering). [Which pin is which?](http://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering)

`GND Pin` `<---[SWITCH]--->` `Pin 18`

### Software

[Create a Raspbian SD card](https://www.raspberrypi.org/documentation/installation/installing-images/) or continue if you already have one.

Log in to Raspberry Pi.

[Set up hostname.](http://www.howtogeek.com/167195/how-to-change-your-raspberry-pi-or-other-linux-devices-hostname/) For example, name it `bathroom-door-sensor`. *Note: some networks won't let you access via hostname if going from WiFi-to-Ethernet or the other way around.*

Install pip: `sudo apt-get python-pip`

Clone this repo: `git clone https://github.com/juxtinteractive/vacant.git`. This will clone into a folder `vacant`.

Install python dependencies: `sudo pip install -r /home/pi/vacant/rpi/requirements.txt`


## Client setup

Clone this repo on the machine that will serve the client app. You could run it on the same Raspberry Pi used for the switch server.

In [`client/index.html`](client/index.html), change `SWITCH_SERVER_URL` to `http://yourhostname.local` where `yourhostname` is the hostname you set up earlier for the Raspberry Pi (or use the RPi's IP address). Example: `var SWITCH_SERVER_URL = 'http://bathroom-door-sensor.local';`.

Start a HTTP server and serve the [`client`](client/) as root.

Assuming the RPi switch server is on and reachable through the network you'll now be able to switch the vacancy sign on an off with the sensor.
