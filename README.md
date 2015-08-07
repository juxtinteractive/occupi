Vacant
######

Is the bathroom vacant? Find out by using a Raspberry Pi's GPIO to keep track of if the door is closed*, and display it on a web page.

* Adapt to some other on/off state application by attaching a different type of switch.


## Raspberry Pi setup

The Raspberry Pi is used as a switch state server, but it could also be used to serve the client web app too.


### Hardware setup

Hook up the switch between the ground pin and GPIO pin `18` (BCM numbering). [Which pin is which?](http://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering)


### Software setup

Set up Raspberry Pi as if new (Raspbian).

Set up static ip


Install pip
	sudo apt-get python-pip

Clone this repo
	git clone git://blablabla

Install Flask and flask-cors (can this be done with pip file?)
	sudo pip install Flask
	sudo pip install flask-cors


On client
#########

In `client/index.html`, edit `SENSOR_SERVER_URL` to whatever IP address the Raspberry Pi has.

Serve the `client` folder in this repo and navigate to it.