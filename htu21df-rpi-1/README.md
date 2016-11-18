#HTU21DF Demo 1

The files in the directory go along with a post on the [IRI Blog site](http://www.iri.com/blog).

* hourly-tmp-hum_ddl.sql - Create table statements for the database table.
* HTU21DF_iri.py - Python script for RPi to read sensors and publish to MQTT broker.
* htu21df-hourly.scl - CoSort SortCL script to aggregate sensor readings and insert into the database table.
* iri-data-subscribe.py - Python script to subscribe to messages, write to intermediate files, and process with SortCL.
