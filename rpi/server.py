## Set up GPIO
import RPi.GPIO as GPIO

SENSOR_PIN = 18  # We're detecting input on pin 18

# A pull up resistor is considered active when there's a low voltage (e.g. False)
PUD_UP_STATE_ON = False
PUD_UP_STATE_OFF = True

GPIO.setmode(GPIO.BCM)  # reference pins by "Broadcom SOC Model"
# See: http://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering

GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # configure SENSOR_PIN
# See: http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/


# Set up server
from flask import Flask, jsonify
from flask.ext.cors import CORS
import random

# initialize random generator
random.seed(1)

app = Flask(__name__)  # create Flask app
cors = CORS(app)  # Allow all origin access to Flask routes


# setup root route
@app.route('/')
def get_status():
  retDict = { 'sensor_status':0 }  # prep a dictionary to be sent as response

  input_state = GPIO.input(SENSOR_PIN)  # get the state of the sensor pin

  if input_state == PUD_UP_STATE_ON:
  	retDict['sensor_status'] = 1

  # return json response
  return jsonify(retDict)


# only start server if this file is run as main program
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
