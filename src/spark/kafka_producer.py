"""
Partially from https://github.com/confluentinc/confluent-kafka-python, code was/is under licence Apache 2.0.
"""
from confluent_kafka import Producer



def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to topic {} partition [{}]'.format(msg.topic(), msg.partition()))



def producer(server_string='localhost,\
            ec2-54-187-33-148.us-west-2.compute.amazonaws.com,\
            ec2-52-40-90-99.us-west-2.compute.amazonaws.com,\
            ec2-52-43-209-134.us-west-2.compute.amazonaws.com'):
    p = Producer({'bootstrap.servers': server_string})
    return p



def send_blob_to_prod(p, topic, data, callback=delivery_report)
    p.produce(topic, data.encode('utf-8'), callback=callback)
    p.flush()

