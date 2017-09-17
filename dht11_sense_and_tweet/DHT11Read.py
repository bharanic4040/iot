import Adafruit_DHT
import influx
import time
import send_tweet


while True:
    humid, temp = Adafruit_DHT.read_retry(11, 27)  # GPIO27 (BCM notation)
    print ("Humidity = {} %; Temperature = {} C".format(humid, temp)) 
    influx.main(str(temp),str(humid)) 
    send_tweet.send_tweet(temp,humid) 
    time.sleep(1) 
