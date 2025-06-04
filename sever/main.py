from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
from sqlalchemy import  LargeBinary,Column, TEXT, VARCHAR,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid
import bcrypt
app = FastAPI()
DATABASE_URL = 'postgresql://postgres:ldv@localhost:5432/flutterspotifyapp'
engine = create_engine(DATABASE_URL)
SessinLocal = sessionmaker(autoflush=False,bind=engine)
db = SessinLocal()
Base = declarative_base()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class User(Base):
    __tablename__  = 'users'
    id = Column(TEXT,primary_key= True)
    name = Column(VARCHAR(100))
     
    email = Column(VARCHAR(100))
    password = Column(LargeBinary)
    
    
@app.post('/signup')
def signup_user(user: UserCreate):
    user_db = db.query(User).filter(User.email == user.email).first()
    
    if user_db:
        raise HTTPException(400,'User with the same email already exists!')
        return 
    
    hasshed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_db = User(id=str(uuid.uuid4()), email=user.email, password=hasshed_pw, name=user.name)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db
Base.metadata.create_all(engine)