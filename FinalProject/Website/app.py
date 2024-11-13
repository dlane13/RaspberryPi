from flask import Flask, render_template, request
import json
import time

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

@app.route('/click-button', methods=["GET"])
def click_button():
    return json.dumps(print_conveyor_status())

def print_conveyor_status():
    print("Running the conveyor belt now!")
    time.sleep(5)
    return "Conveyor belt has finished running! The printer is ready for your next project."

@app.route('/OctoPrint', methods=["GET"])
def OctoPrint():
    return render_template("OctoPrint.html")

@app.route('/FailureDetection', methods=["GET"])
def FailureDetection():
    return render_template("FailureDetection.html")
