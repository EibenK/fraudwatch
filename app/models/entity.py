from sqlalchemy import Column, String, Float, Integer
from app.db import Base

class Entity(Base):
    __tablename__ = "entities"

    entity_id = Column(String, primary_key=True, index=True)
    entity_type = Column(String, nullable=False)
    avg_amount = Column(Float, nullable=False)
    tx_per_min = Column(Integer, nullable=False)
    country = Column(String, nullable=False)
    risk_level = Column(String, nullable=False)


if __name__ == "__main__":
    pass