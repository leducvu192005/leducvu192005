from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DATABASE_URL = 'postgresql://postgres:ldv@localhost:5432/flutterspotifyapp'
engine = create_engine(DATABASE_URL)
SessinLocal = sessionmaker(autoflush=False,bind=engine)

def get_db():
    db = SessinLocal()
    try:
        yield db
    finally:
        db.close()

