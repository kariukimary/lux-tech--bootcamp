# lux-tech--bootcamp
ML &amp; Data engineering
# Importing Csv_file to postgres_databases
<img width="730" alt="imp1" src="https://github.com/kariukimary/lux-tech--bootcamp/assets/133002438/49e71778-11d8-4a50-8f16-371a7d1188a0">

The code above i imported all the required libraries, listed the database connection details, imported my data using pandas, removed unneccesary columns, and finally  changed the date to datetime format.

<img width="740" alt="imp2" src="https://github.com/kariukimary/lux-tech--bootcamp/assets/133002438/607f4b76-8be5-44fd-9a50-910c5c2d2e22">

i  created the table  with the exact column names of my dataset and execute

<img width="781" alt="imp3" src="https://github.com/kariukimary/lux-tech--bootcamp/assets/133002438/02b2a594-4d1f-498d-83d2-3c78dd483f57">

i  now copied the csv_file to the table in my  postgress database , and data was successfully imported to postgress

# Migrating data  from postgress to snowflake
i used airbyte to create the connection from postgres to snowflake. i created the connection at airbyte  after getting the details from  cloud database called supabase where i found it easier to create my database once again in an easier way for easier migration of the data.

creating connection at airbyte

<img width="511" alt="connection in airbyte" src="https://github.com/kariukimary/lux-tech--bootcamp/assets/133002438/60ad3362-cc32-415e-93b3-8586665f2911">

using supabase to connect the local database with the cloud database

<img width="954" alt="supabase" src="https://github.com/kariukimary/lux-tech--bootcamp/assets/133002438/d547fbd7-2ae3-40fd-91f0-2e80559e7596">

creating the table at snowflake 

<img width="960" alt="table_snowflake" src="https://github.com/kariukimary/lux-tech--bootcamp/assets/133002438/121514f8-f927-4937-881c-faf70cbd26ef">

