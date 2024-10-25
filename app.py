from flask import Flask, jsonify, request, abort
from flask_mysqldb import MySQL
from config import Config
from utils import addBooking, allFlights, allBookings, getByPriceUtil

app = Flask(__name__)
app.config.from_object(Config)

# Initialize MySQL
mysql = MySQL(app)



@app.route("/all-flights", methods=["GET"])
def getAllflights():
    data=allFlights(mysql=mysql, request=request)
    return jsonify(data)

@app.route("/all-bookings", methods=["GET"])
def getAllbookings():
    data=allBookings(mysql=mysql)
    return jsonify(data)

@app.route("/add-bookings", methods=["POST"])
def addBookingMain():
    addBooking(mysql, request)
    return jsonify({"message":"booking successfully added"})

@app.route("/price", methods=["POST"])
def getByPrice():
    data=getByPriceUtil(mysql=mysql, request=request)
    return jsonify(data)





if __name__=="__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
