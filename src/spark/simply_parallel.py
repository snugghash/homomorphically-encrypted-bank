"""
Homomorphic encryption implemented by using existing PySEAL. Horizontal scaling. 
"""
from pyspark.sql import SparkSession
from kafka_consumer import kafka_consumer_gen
import seal

logFile = "input.txt"  # Should be some file on your system
spark = SparkSession.builder.appName("simply_parallel.py").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()
