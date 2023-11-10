import psycopg2
import pandas as pd
from io import StringIO

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    user = "postgres",
    password = "chatme@2023",
    database = "mydb"
)

#create a cursor object
cur = conn.cursor()


data = pd.read_csv('craigslist_vehicles.csv')

cols = ['Unnamed: 0', 'url', 'region_url', 'VIN', 'county', 'state', 'description']
data.drop(data[cols], axis=1, inplace=True)

# parse dates
data['posting_date'] = pd.to_datetime(data['posting_date'])
data['removal_date'] = pd.to_datetime(data['removal_date'])



columns = data.columns.tolist()

for column in columns:
    if data[column].dtype == 'object':
        data[column] = data[column].fillna('?')
    else:
        data[column] = data[column].fillna(0)
data = data.drop(4986, axis=0)



create_table = """CREATE TABLE IF NOT EXISTS vehicles (
    id BIGINT PRIMARY KEY,
    region VARCHAR(255),
    price INT,
    year NUMERIC,
    manufacturer VARCHAR(255),
    model VARCHAR(255),
    condition VARCHAR(255),
    cylinders VARCHAR(255),
    fuel VARCHAR(255),
    odometer NUMERIC,
    title_status VARCHAR(255),
    transmission VARCHAR(255),
    drive VARCHAR(255),
    size VARCHAR(255),
    type VARCHAR(255),
    paint_color VARCHAR(255),
    image_url VARCHAR(255),
    lat FLOAT,
    long FLOAT,
    posting_date DATE,
    removal_date DATE
);"""


cur.execute(create_table)
conn.commit()
print("Table created successfully")

data = data.iloc[:6000]
data.to_csv('output.csv', index=False)
with open('output.csv', 'r') as f:
    next(f) # Skip the header row.
    cur.copy_from(f, 'vehicles', sep=',')

conn.commit()
cur.close()
print("CSV data imported successfully")
