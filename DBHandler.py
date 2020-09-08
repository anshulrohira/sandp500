import  mysql.connector
import  os
import pandas as pd

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    db="SandP500DB",
    auth_plugin="mysql_native_password",
    allow_local_infile=True,
    autocommit=True
)

def Df_to_MySQL(sp500):
    try:
        sp500.to_csv("../CachedPickles/sp500tickers.csv")
        cursor = db_connection.cursor()
        cursor.execute("""
        LOAD DATA LOCAL INFILE '../CachedPickles/sp500tickers.csv' INTO TABLE SandP500
        FIELDS TERMINATED BY ',' 
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;
        """)
        db_connection.close()
        os.remove("../CachedPickles/sp500tickers.csv")
    except Exception as e:
        print(e)
