from flask import Flask, render_template, request
import json
import time

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("HomePage.html")

@app.route("/conveyor_button", methods=["GET"])
def conveyor_button():
    print("The conveyor belt is running...")
    time.sleep(5)
    return "The conveyor belt has finished running. Your printer is ready for your next crazy idea!"

@app.route('/HomePage', methods=['GET'])
def HomePage():
    return render_template("HomePage.html", name="Darby Lane")

@app.route('/ConveyorBelt', methods=['GET'])
def ConveyorBelt():
    return render_template("ConveyorBelt.html", name="Darby Lane")
