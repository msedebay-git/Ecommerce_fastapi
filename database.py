from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# DATABASE_URL = "postgresql://username:password@localhost:5432/ecommerce_db"
DATABASE_URL1 = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL1)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()