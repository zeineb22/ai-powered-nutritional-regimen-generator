from sqlmodel import SQLModel, create_engine, Session
import os

# URL SYNCHRONE - sans asyncpg
DATABASE_URL = "postgresql://appuser:apppass@postgres:5432/nutritiondb"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
