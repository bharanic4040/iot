import Adafruit_DHT
import influx
import time
import send_tweet

# connection settings on the breadboard
#--------------------------------------
#DHT 11 temp and humidity sensor
#connect leftmost to  5v pin
# 2 pin on dht to 4th gpio pin
# 3 pin unused
# 4 pin to ground
#1kohm resistor between 1 and 2 dht pins

while True:
    humid, temp = Adafruit_DHT.read_retry(11, 4)  # GPIO4 (BCM notation)
    print ("Humidity = {} %; Temperature = {} C".format(humid, temp)) 
    #influx.main(str(temp),str(humid)) 
    send_tweet.send_tweet(temp,humid) 
    time.sleep(5) 
