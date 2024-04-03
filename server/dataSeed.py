import mysql.connector

# Database configuration
config = {
    'user': 'ru87lutk79os69pl',
    'password': 'y03wbzy8ellowdcs',
    'host': 'uc13jynhmkss3nve.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
    'database': 's6cidla3ltlvdz9y'
}

# Data to be inserted
data = [
    (1232476002, "970 10TH ST, WAUKEE", "$1,423,422", "6/17/2022", None, "2022-14379", "$17,560", 2024, 474474, 908, "N", "Office - General"),
    # Add more data as needed
]

# Connect to the database
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# SQL command to insert data into the table
insert_query = """
INSERT INTO property_data (ParcelID, Address, SalePrice, SaleDate, MultiParcelSale, Recording, AssessedValue, YearBuilt, LotArea, BuildingArea, Vacant, Occupancy)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Execute the SQL command to insert data
cursor.executemany(insert_query, data)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
