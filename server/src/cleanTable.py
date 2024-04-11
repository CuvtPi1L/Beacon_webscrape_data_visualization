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

# List of table names to drop
tables_to_drop = ['table1', 'table2', 'table3']

for table in tables_to_drop:
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table};")
        print(f"{table} has been dropped.")
    except mysql.connector.Error as err:
        print(f"Failed to drop {table}: {err}")

conn.commit()
cursor.close()
conn.close()
