#!/usr/bin/python
import paho.mqtt.client as mqtt

prev_filename = None

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with broker, result code: " + str(rc))

	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe("/iri/data/piot")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	global prev_filename
	filename = str('piot/' + str(msg.payload)[0:13] + '.txt')
	if filename != prev_filename:
		if prev_filename is not None:
			print('post_process(' + prev_filename + ')')
			post_process(prev_filename)
		prev_filename = filename
	print(str(msg.payload))
	logfile = open(filename, 'a')
	logfile.write(str(msg.payload) + '\n')
	logfile.close()

# Calls sortcl to process the previous hour's data, stores in a MySQL database.
def post_process(filename):
	import subprocess, os
	my_env = os.environ.copy()
	my_env['INFILE'] = filename
	subprocess.Popen(['sortcl', '/SPECIFICATION=htu21df-hourly.scl'], env=my_env)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mangled.iri.com")
client.loop_forever()
