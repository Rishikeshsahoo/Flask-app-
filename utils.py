def allFlights(mysql, request):
    cursor = mysql.connection.cursor()
    source= request.args.get("source")
    destination= request.args.get("destination")

    print(source)
    print(destination)


    if(source==None or destination==None):
        cursor.execute("SELECT * FROM flights")
    else :
        cursor.execute("SELECT * FROM flights where source = %s and destination = %s", (source, destination))
    flights = cursor.fetchall()
    cursor.close()
    return flights

def allBookings(mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM bookings")
    flights = cursor.fetchall()
    cursor.close()
    return flights

def addBooking(mysql, request):
    user_id = request.json['user_id']
    flight_id = request.json['flight_id']
    booking_date = request.json['booking_date']
    status = request.json.get('status', 'pending')  

    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO bookings (user_id, flight_id, booking_date, status) VALUES (%s, %s, %s, %s)",
        (user_id, flight_id, booking_date, status)
    )
    mysql.connection.commit()
    cursor.close()

    return {"message": "Booking added successfully"}



def getByPriceUtil(mysql, request):
    cursor = mysql.connection.cursor()
    price = request.json['price']

    cursor.execute(f"SELECT * FROM flights where price < {price}")
    flights = cursor.fetchall()
    cursor.close()
    return flights