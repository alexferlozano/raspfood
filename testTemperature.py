import time
import board
import adafruit_dht
import requests
from datetime import datetime

dhtDevice = adafruit_dht.DHT11(board.D18)

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
    

while True:
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
        now = datetime.now()
        data = {'value_int':1, 'value_float': temperature_c, 'value_string':'null', 'date':now.isoformat(), 'raspberry_sensor_id': '2'}
        r = requests.post('https://alimdogandcat.space/SensorValues/Create', json=data, auth=BearerAuth('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjEsImlhdCI6MTY2NzU4ODQ0MH0.2fTbZWJTcDwvibU9nPefDFq8LSdQjMDXx4OxUbOpCwY'))
        #post = r.json()
        if r.status_code == 200:
            rp = r.json()
            print(rp)
        else:
            print("Error from server: " + str(r.content))

    except RuntimeError as error:
        dhtDevice.exit()
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)