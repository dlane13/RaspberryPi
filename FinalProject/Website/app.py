from flask import Flask, render_template, jsonify
import time
import board
from adafruit_motorkit import MotorKit

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("HomePage.html")

@app.route('/HomePage', methods=['GET'])
def HomePage():
    return render_template("HomePage.html")

@app.route('/ConveyorBelt', methods=['GET'])
def ConveyorBelt():
    return render_template("ConveyorBelt.html")

@app.route('/conveyor_on', methods=["POST"])
def click_button():
    kit = MotorKit(i2c=board.I2C())
    kit.motor1.throttle = 1
    time.sleep(2)
    kit.motor1.throttle = 0
    return "Conveyor activated" 

@app.route('/OctoPrint', methods=["GET"])
def OctoPrint():
    return render_template("OctoPrint.html")

@app.route('/FailureDetection', methods=["GET"])
def FailureDetection():
    return render_template("FailureDetection.html")
