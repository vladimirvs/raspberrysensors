import time
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

db_connection = mysql.connector.connect(
  host="localhost",
  user="acv",
  passwd="P@ssw0rd",
  database="sensors"
)
print(db_connection)
db_connection.autocommit = True

def readRecords(cnt):
    db_connection.reconnect()
    db_cursor = db_connection.cursor()
    sql_query = """SELECT * FROM temphum ORDER BY sampled DESC LIMIT %s"""
    
    db_cursor.execute(sql_query, (cnt,))
    records = db_cursor.fetchall()
    print("Total number of rows fetched: ", db_cursor.rowcount)
    for row in records:
        print("Id = ", row[0], )
        print("Temp = ", row[1])
        print("Humi = ", row[2])
        print("Date  = ", row[3], "\n")
    db_cursor.close()
    return records

@app.route("/")
def main():
   record_data = readRecords(30) 

  # templateData = {
 #     'records' : records
  # }
   #if humidity is not None and temperature is not None:
   # print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
   return render_template('main.html', records = record_data)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True, threaded=True)

