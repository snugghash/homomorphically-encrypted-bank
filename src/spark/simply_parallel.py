"""
Homomorphic encryption implemented by using existing PySEAL. Horizontal scaling. 

Sources: Spark quickstart
https://www.rittmanmead.com/blog/2017/01/getting-started-with-spark-streaming-with-python-and-kafka/
"""
from pyspark.sql import SparkSession
# SparkSession is newer, recommended API over SparkContext
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
from kafka_consumer import kafka_consumer_gen
import seal



# Streaming test
sc = SparkContext(appName="simply_parallel_HE")
sc.setLogLevel("WARN")

ssc = StreamingContext(sc, 10)
kafkaStream = KafkaUtils.createStream(ssc, 'ec2-52-11-165-61.us-west-2.compute.amazonaws.com:2181', 'spark-streaming', {'eth-old':1})

#parsed = kafkaStream.map(lambda datapoint: dict(datapoint))
kafkaStream..pprint()

ssc.start()
ssc.awaitTermination()
