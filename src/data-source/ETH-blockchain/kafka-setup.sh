kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 3 --topic test
kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 3 --topic eth-old
kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 3 --topic eth-old-decrypted
python3 kafka_producer.py
