import hashlib
import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer


class KafkaProducerClass:
    def __init__(self, amt_to_generate=1, batch_interval=2):
        producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

        self.topic = "transactions_stream"
        self._transaction_db = {}

        self.generate_transactions(amt_to_generate)
        self.produce_batch(batch_interval)
    
    def generate_transactions(self, amt):
        for _ in range(amt):
            txn = self.generate_transaction()
            txn_id_hash = self.hash_transaction(txn)
            self._transaction_db[txn_id_hash] = txn

    def generate_transaction(self):
        return {
            "transaction_id": f"tx_{random.randint(10000,99999)}",
            "user_id": f"user_{random.randint(1, 100)}",
            "amount": round(random.uniform(1, 10000), 2),
            "currency": "USD",
            "timestamp": datetime.utcnow().isoformat(),
            "ip_address": f"192.168.1.{random.randint(1,255)}",
            "country": random.choice(["US", "GB", "DE", "IN", "RU"]),
            "merchant": random.choice(["Amazon", "BestBuy", "Target"]),
            "card_type": random.choice(["VISA", "MASTERCARD"]),
            "device_id": f"device_{random.randint(1000,9999)}"
        }

    def hash_transaction(self, txn):
        txn_str = json.dumps(txn, sort_keys=True)
        return hashlib.sha256(txn_str.encode('utf-8')).hexdigest()

    def produce_batch(self, interval):
        while True:
            for txn_id, txn_data in self._transaction_db.items():
                self.producer.send(self.topic, value=txn_data)
                print(f"Produced {txn_id}: {txn_data}")
            self._transaction_db.clear()
            time.sleep(interval)



if __name__ == "__main__":
    producer = KafkaProducerClass(10, 5)
