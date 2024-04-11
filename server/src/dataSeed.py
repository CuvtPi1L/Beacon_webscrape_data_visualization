import mysql.connector
import pandas as pd

# Database configuration
config = {
    'user': 'ru87lutk79os69pl',
    'password': 'y03wbzy8ellowdcs',
    'host': 'uc13jynhmkss3nve.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
    'database': 's6cidla3ltlvdz9y'
}

csv_file_path = 'Beacon_webCrawl - Sheet2.csv' 


# Connect to the database
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

df = pd.read_csv(csv_file_path)

# Data preprocessing
df['SalePrice'] = df['SalePrice'].replace('[\$,]', '', regex=True).astype(float)
df['AssessedValue'] = df['AssessedValue'].replace('[\$,]', '', regex=True).astype(float)
df['SaleDate'] = pd.to_datetime(df['SaleDate']).dt.strftime('%Y-%m-%d')  # Format date for MySQL

# Insert data into the database
for index, row in df.iterrows():
    cursor.execute('''
    INSERT INTO real_estate (ParcelID, Address, SalePrice, SaleDate, MultiParcelSale, Recording, AssessedValue, YearBuilt, LotArea, BuildingArea, Vacant, Occupancy, TaxDistrict)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (row['Parcel ID'], row['Address'], row['SalePrice'], row['SaleDate'], row['MultiParcelSale'], row['Rec-ording'], row['AssessedValue'], row['YearBuilt'], row['LotArea(sf)'], row['BuildingArea'], row['Vacant'], row['Occupancy'], row['Tax District']))



conn.commit()
cursor.close()
conn.close()
