"""
Partially from https://github.com/confluentinc/confluent-kafka-python, code was/is under licence Apache 2.0.
"""
from confluent_kafka import Producer
from read_from_BigQuery import get_data_from_BigQuery_continuous_stateful



# TODO move to env files
p = Producer({'bootstrap.servers': 'localhost,\
        ec2-54-187-33-148.us-west-2.compute.amazonaws.com,\
        ec2-52-40-90-99.us-west-2.compute.amazonaws.com,\
        ec2-52-43-209-134.us-west-2.compute.amazonaws.com'})



def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to topic {} partition [{}]'.format(msg.topic(), msg.partition()))



for data in get_data_from_BigQuery_continuous_stateful(100):
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    for row in data:
        p.produce('eth-old', row['value'].encode('utf-8'), callback=delivery_report)



# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()
