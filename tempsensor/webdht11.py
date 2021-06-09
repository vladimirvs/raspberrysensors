import Adafruit_DHT
import time
from flask import Flask, render_template

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

app = Flask(__name__)

@app.route("/")
def main():
   humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
   templateData = {
      'temperature' : temperature,
      'humidity': humidity
   }
   if humidity is not None and temperature is not None:
    print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)

