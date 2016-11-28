#Using SortCL to Aggregate IoT Data

###Executing From Python

The data aggregation and preparation is performed not in the Python script, but by IRI CoSort in a SortCL job script that gets executed by the Python script. In this demonstaqtion, the aggregation is performed on the subscriber side of the broker. The following Python code executes the SortCL script:
```python 
my_env['INFILE'] = filename
subprocess.Popen(['sortcl', '/SPECIFICATION=htu21df-hourly.scl'], env=my_env)
```
###The SortCL script

The /INFILE statement specifies the name of one or more data sources, which is in this case is an environment variable (EV) which will be set to a file written by our Python script. The ALIAS statement creates a logical name for a physical file that can be used wherever it may be referenced later in the script. The input file has 3 fields (timestamp, temperature, and humidity), and we describe the type of input. 

The /INREC section provides a common record layout for use by the action phase of SortCL and subsequent processing. Station ID is the field value indicated the source of the data. So we declare it as 1. In our second field we are setting up the hourly sample period by masking the minutes and seconds in the timestamp with zeros. Fields 3 and 4 are the temperature and humidity..

We store the aggregated values, along with the station ID, hourly period, and count of the number of data points, in the location specified in the /OUTFILE statement. In this case, it  is a MySQL table, connected to with ODBC. We declare field, position, and data type for each field. The EXT_FIELD attribute refers to the column name in the table in which to store the value. The aggregation continues until it hits a break condition (the hourly period), or until the end of the data. In this way, the same script may be used to process data from multiple hourly periods at once, as long as the data is sorted in chronological order. 