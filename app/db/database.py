import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DB_URL =  (
    f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@localhost:"
    f"{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()