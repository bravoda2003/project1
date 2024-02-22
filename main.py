import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Bravoda@2003'
)
myc = mydb.cursor()

myc.execute("CREATE DATABASE emanual")

mydb = msql.connector.connect(

)