import mysql.connector

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

# SQL command to create a table
create_table_query = """
CREATE TABLE property_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ParcelID VARCHAR(255),
    Address VARCHAR(255),
    SalePrice VARCHAR(255),
    SaleDate VARCHAR(255),
    MultiParcelSale VARCHAR(255),
    Recording VARCHAR(255),
    AssessedValue VARCHAR(255),
    YearBuilt INT,
    LotArea DECIMAL(18, 2),
    BuildingArea DECIMAL(18, 2),
    Vacant VARCHAR(1),
    Occupancy VARCHAR(255),
    TaxDistrict VARCHAR(255)
)
"""

# Execute the SQL command to create the table
cursor.execute(create_table_query)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
