import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

 
app = Flask(__name__, static_folder = "client/build")
CORS(app)
# Database configuration
config = {
    'user': 'ru87lutk79os69pl',
    'password': 'y03wbzy8ellowdcs',
    'host': 'uc13jynhmkss3nve.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
    'database': 's6cidla3ltlvdz9y'
}

# Connect to the database
conn = mysql.connector.connect(**config)
cursor = conn.cursor()




# Seed the database
@app.route('/seed')
def seed_database():
    # Example data
    data = [
        (1232476002, "970 10TH ST, WAUKEE", "$1,423,422", "6/17/2022", None, "2022-14379", "$17,560", 2024, 474474, 908, "N", "Office - General"),
        # Add more data as needed
    ]

    # Insert data into the database
    for item in data:
        cursor.execute("INSERT INTO property_data (ParcelID, Address, SalePrice, SaleDate, MultiParcelSale, Recording, AssessedValue, YearBuilt, LotArea, BuildingArea, Vacant, Occupancy) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", item)

    # Commit changes
    conn.commit()

    return "Data seeded successfully!"

@app.route('/api/data')
def get_data():
    try:
        # Connect to the database
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor(dictionary=True)

        # Fetch data from the database
        cursor.execute("SELECT * FROM property_data")
        data = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Return data as JSON response
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
