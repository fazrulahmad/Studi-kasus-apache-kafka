# Studi Kasus Apache Kafka

| Nama                                                | NRP        |
| --------------------------------------------------- | ---------- |
| Fazrul Ahmad Fadhilah                               | 5027221025 |
| Asadel Naufaleo                                     | 5027221009 |

## Menjalankan server zookeeper dan kafka
Pada studi kasus ini, kami menjalankan server zookeeper dan kafka melalui WSL, berikut adalah langkah-langkah untuk menjalankan servernya:
- Install openJDK dengan command `sudo apt install wget openjdk-11-jre -y`
- Download kafka dengan command `wget https://downloads.apache.org/kafka/3.8.1/kafka_2.13-3.8.1.tgz`
- Ekstrak filenya dengan command `tar -xzf kafka_2.13-3.8.1.tgz`
- Lalu masuk ke direktori kafka dengan command `cd kafka_2.13-3.8.1`
- Pada WSL, buka 2 tab untuk menjalankan zookeeper dan kafka server, urutan menjalankannya adalah zookeeper terlebih dahulu. dengan command `bin/zookeeper-server-start.sh config/zookeeper.properties` untuk zookeeper dan `bin/kafka-server-start.sh config/server.properties` untuk kafka server
- Buatlah topik di tab baru dongan command `bin/kafka-topics.sh --create --topic sensor-suhu --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`

## Menjalankan producer dan consumer
Urutan untuk menjalankannya adalah producer terlebih dahulu.
- Pindah ke direktori **studi kasus apache kafka**, lalu masukkan command `python producer.py`, di sini kita dapat melihat data suhu yang dikirim ke topik sensor-suhu
- Buka terminal baru untuk menjalankan consumer, pindah ke direktori **studi kasus apache kafka**, lalu masukkan command `spark-submit consumer.py` untuk menjalankan consumer dan memfilter data suhu yang di atas 80.