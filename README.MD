# FraudWatch — Real-Time Transaction Fraud Detection System

FraudWatch is a real-time fraud detection pipeline built to simulate, process, and flag suspicious financial transactions. It combines synthetic transaction generation, streaming pipelines, and fraud heuristics to model real-world behaviors across different entity types like individuals, companies, or high-risk profiles.

---

## Purpose

To build a modular and scalable system that simulates real-time financial activity and detects fraudulent behavior using behavioral patterns, statistical outliers, and real-time alerting mechanisms.

---

## Project Goals

- Build entity-specific transaction simulators using realistic profiles stored in a Postgres SQL database.
- Stream transactions to a Kafka topic for downstream processing and fraud evaluation.
- Apply rule-based and ML-based detection to score transaction risk.
- Enable real-time alerting and logging for suspicious activity.
- Architect the pipeline to support modular expansion and eventual deployment at scale.

---

## Tech

- Libraries: hashlib, psycopg2-binary, sqlalchemy, alembic, dotenv
- Technologies: Kafka, FastAPI, Docker, Docker-Compose, PostgresSQL

