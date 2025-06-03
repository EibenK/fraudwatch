from app.db import engine
from app.models.entity import Entity

Entity.__table__.create(bind=engine, checkfirst=True)
