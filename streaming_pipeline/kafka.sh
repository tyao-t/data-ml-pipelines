sudo yum install -y java
pip install --user kafka-python
wget https://downloads.apache.org/kafka/3.2.0/kafka_2.12-3.2.0.tgz

tar -xzf kafka_2.12-3.2.0.tgz

cd kafka_2.12-3.2.0
bin/zookeeper-server-start.sh config/zookeeper.properties
 
# new terminal
bin/kafka-server-start.sh config/server.properties
 
# new terminal
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic streaming_pipeline

# Sklearn pipeline
vi config/server.properties 
advertised.listeners=PLAINTEXT://{aws_external_ip}:9092
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 
                --replication-factor 1 --partitions 1 --topic predictions