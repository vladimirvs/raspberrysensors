import Adafruit_DHT
import time
import mysql.connector

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

db_connection = mysql.connector.connect(
  host="localhost",
  user="acv",
  passwd="P@ssw0rd",
  database="sensors"
)
print(db_connection)

prev_temp = None
prev_humi = None

def insertRecord(temp, hum):
    db_cursor = db_connection.cursor()
    sql_query = """INSERT INTO temphum (temperature, humidity, sampled) VALUES (%s, %s, NOW())"""
    tupl = (temp, hum)
    db_cursor.execute(sql_query, tupl)
    db_connection.commit()
    print(db_cursor.rowcount, "Record Inserted")



while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.2f}C Humidity={1:0.2f}%".format(temperature, humidity))
        print ("T = "+str(temperature)+" H = "+str(humidity))
        if temperature != prev_temp or humidity != prev_humi:
            insertRecord(temperature, humidity)
            prev_temp = temperature
            prev_humi = humidity
        else:
            print("Temp and Humidity unchanged. Not inserting in the DB")
    else:
        print("Sensor failure. Check wiring.")
    time.sleep(3);



    
