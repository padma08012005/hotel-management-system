from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample Hotel Data
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Extended Hotel Data
hotels = [
    # Chennai
    {"name": "Taj Palace", "city": "Chennai", "price": 5500, "rating": 4.8,
     "features": ["AC", "Spa", "Hot Water", "Free WiFi"]},

    {"name": "Chennai Comfort Inn", "city": "Chennai", "price": 3000, "rating": 4.0,
     "features": ["AC", "Free WiFi"]},

    # Mumbai
    {"name": "The Shelton Grand", "city": "Mumbai", "price": 4500, "rating": 4.5,
     "features": ["AC", "Hot Water", "Restaurant"]},

    {"name": "Mumbai Sea View", "city": "Mumbai", "price": 6000, "rating": 4.9,
     "features": ["AC", "Spa", "Swimming Pool", "Hot Water"]},

    # Hyderabad
    {"name": "Hyderabad Residency", "city": "Hyderabad", "price": 4000, "rating": 4.2,
     "features": ["Non-AC", "Hot Water", "Free WiFi"]},

    {"name": "Royal Palace Hyderabad", "city": "Hyderabad", "price": 5200, "rating": 4.6,
     "features": ["AC", "Spa", "Hot Water", "Restaurant"]},

    # Delhi
    {"name": "Delhi Grand Hotel", "city": "Delhi", "price": 5000, "rating": 4.4,
     "features": ["AC", "Hot Water", "Free WiFi", "Restaurant"]},

    {"name": "Capital Stay Delhi", "city": "Delhi", "price": 3800, "rating": 4.1,
     "features": ["AC", "Free WiFi"]},

    # Kolkata
    {"name": "Kolkata Royal Inn", "city": "Kolkata", "price": 4200, "rating": 4.3,
     "features": ["AC", "Hot Water", "Restaurant"]},

    {"name": "Howrah Comfort Stay", "city": "Kolkata", "price": 3200, "rating": 4.0,
     "features": ["Non-AC", "Hot Water"]},

    # Bangalore
    {"name": "Bangalore Tech Park Hotel", "city": "Bangalore", "price": 4800, "rating": 4.7,
     "features": ["AC", "Free WiFi", "Spa"]},

    {"name": "Garden City Residency", "city": "Bangalore", "price": 3500, "rating": 4.2,
     "features": ["AC", "Hot Water"]},

    # Jaipur
    {"name": "Jaipur Heritage Palace", "city": "Jaipur", "price": 5300, "rating": 4.6,
     "features": ["AC", "Spa", "Restaurant"]},

    {"name": "Pink City Lodge", "city": "Jaipur", "price": 2800, "rating": 3.9,
     "features": ["Non-AC", "Hot Water"]},

    # Goa
    {"name": "Goa Beach Resort", "city": "Goa", "price": 7000, "rating": 4.9,
     "features": ["AC", "Swimming Pool", "Spa", "Hot Water"]},

    {"name": "Sunset Goa Stay", "city": "Goa", "price": 4500, "rating": 4.4,
     "features": ["AC", "Free WiFi"]},

    # Pune
    {"name": "Pune Business Hotel", "city": "Pune", "price": 4100, "rating": 4.3,
     "features": ["AC", "Hot Water", "Free WiFi"]},

    {"name": "Pune Comfort Residency", "city": "Pune", "price": 3000, "rating": 4.0,
     "features": ["Non-AC", "Restaurant"]}
]

@app.route('/')
def welcome():
    return render_template("welcome.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        city = request.form.get("city")
        selected_features = request.form.getlist("features")

        filtered_hotels = []
        for hotel in hotels:
            if hotel["city"] == city:
                if all(feature in hotel["features"] for feature in selected_features):
                    filtered_hotels.append(hotel)

        return render_template("hotels.html", hotels=filtered_hotels, city=city)

    return render_template("dashboard.html")


# Booking Page (NEW)
@app.route('/booking/<hotel_name>', methods=["GET", "POST"])
def booking(hotel_name):
    if request.method == "POST":
        customer_name = request.form.get("name")
        rooms = request.form.get("rooms")
        return redirect(url_for("thankyou", hotel_name=hotel_name, name=customer_name, rooms=rooms))

    return render_template("booking.html", hotel_name=hotel_name)


# Thank You Page
@app.route('/thankyou')
def thankyou():
    hotel_name = request.args.get("hotel_name")
    name = request.args.get("name")
    rooms = request.args.get("rooms")

    return render_template("thankyou.html",
                           hotel_name=hotel_name,
                           name=name,
                           rooms=rooms)


if __name__ == '__main__':
    app.run(debug=True)