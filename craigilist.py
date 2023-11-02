import mysql
from mysql.connector import connect
import pandas as pd


#connecton details
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='chatme@2023',
    database='mydatabase')

cursor=conn.cursor()

df= pd.read_csv('updated_dataset.csv')

cols = ['Unnamed: 0', 'url', 'region_url', 'VIN', 'county','type','long','year', 'state', 'description']
df.drop(df[cols], axis=1, inplace=True)

df['posting_date'] = pd.to_datetime(df['posting_date'])
df['removal_date'] = pd.to_datetime(df['removal_date'])

columns = df.columns.tolist()

for column in columns:
    if df[column].dtype == 'object':
        df[column] = df[column].fillna('?')
    else:
        df[column] = df[column].fillna(0)
df=df.drop(4986, axis=0)

create_table = """CREATE TABLE  IF NOT EXISTS vehicles3 (
    id BIGINT PRIMARY KEY,
    region VARCHAR(255),
    price INT,
    manufacturer VARCHAR(255),
    model VARCHAR(255),
    conditions VARCHAR(255),
    cylinders VARCHAR(255),
    fuel VARCHAR(255),
    odometer INT,
    title_status VARCHAR(255),
    transmission VARCHAR(255),
    drive VARCHAR(255),
    size VARCHAR(255),
    paint_color VARCHAR(255),
    image_url VARCHAR(255),
    lat FLOAT,
    posting_date DATETIME,
    removal_date DATETIME
);"""
cursor.execute(create_table)
conn.commit()
print("Table created successfully")



df = df.iloc[:6000]
df.to_csv('output.csv', index=False)

table_name = 'vehicles3'
df= 'updated_dataset.csv'
load_data_query = f"""
LOAD DATA LOCAL INFILE '{df}' 
INTO TABLE {table_name}
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\\n'
IGNORE 1 LINES; 
"""

conn.commit()
cursor.close()
print("CSV data imported successfully")




        
        
       
       
        

    

   
