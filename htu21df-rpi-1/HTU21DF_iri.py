#!/usr/bin/python

# A simple program to read values from a HTU21DF every 5 seconds, add a timestamp, print 
# them to the screen and publish them to a MQTT broker.

import time
import HTU21DF
import paho.mqtt.client as mqtt

INTERVAL_SECONDS = 5
MQTT_TOPIC = '/iri/data/piot'

client = mqtt.Client()
client.connect("mangled.iri.com")

while True:
	# wait for an even increment of 5 seconds
	while (time.gmtime().tm_sec % INTERVAL_SECONDS) > 0:
		pass

	# collect the data
	try:
		HTU21DF.htu_reset
		temperature = HTU21DF.read_temperature()
		humidity = HTU21DF.read_humidity()

		# format into a record, print to the screen, and publish
		data = str("{:s}\t{:.3f}\t{:.3f}").format(time.strftime("%FT%T"),
				temperature, humidity)
		print(data)
		client.publish(MQTT_TOPIC, data) 

	except:
		pass

	# give the mqtt client a time slice, then sleep for awhile
	client.loop()
	time.sleep(INTERVAL_SECONDS - 1)
