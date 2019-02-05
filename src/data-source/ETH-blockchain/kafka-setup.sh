kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic eth-old
python3 kafka-producer.py
