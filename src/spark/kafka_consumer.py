"""
From https://github.com/confluentinc/confluent-kafka-python, code was/is under Apache 2.0.
? limiting rate?
TODO Analytics
TODO extract URLs to env perhaps
TODO is KafkaError necessary
"""
from confluent_kafka import Consumer, KafkaError



def kafka_consumer_gen(channel_to_sub_to='eth-old'):
    """
    Python generator for consuming from known kafka cluster.
    """
    c = Consumer({
        'bootstrap.servers': 'ec2-52-11-165-61.us-west-2.compute.amazonaws.com,\
                              ec2-52-40-90-99.us-west-2.compute.amazonaws.com,\
                              ec2-34-218-39-83.us-west-2.compute.amazonaws.com',
        'group.id': 'consumer-test',
        'auto.offset.reset': 'earliest'
    })
    c.subscribe([channel_to_sub_to])

    while True:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
        print('Received message: {}'.format(msg.value().decode('utf-8')))
        yield msg.value().decode('utf-8')

    c.close()



if __name__ == "__main__":
    for i in kafka_consumer_gen():
        print(i)
