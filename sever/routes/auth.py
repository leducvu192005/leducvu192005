import bcrypt
from fastapi import HTTPException
from pydantic_schemas.user_create import UserCreate
import uuid
from fastapi import APIRouter, Depends
from models.user import User  
from sqlalchemy.orm import Session
router = APIRouter()
from database import get_db
from pydantic_schemas.user_login import UserLogin 
@router.post('/signup', status_code=201)
def signup_user(user: UserCreate, db: Session=Depends(get_db)):
    # kiểm tra xem người dùng đã tồn tại trong db chưa
    user_db = db.query(User).filter(User.email == user.email).first()

    if user_db:
        raise HTTPException(400, 'Người dùng với email này đã tồn tại!')
    
    hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_db = User(id=str(uuid.uuid4()), email=user.email, password=hashed_pw, name=user.name)
    
    # thêm người dùng vào db
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db
@router.post('/login')
def login_user(user: UserLogin,db: Session = Depends(get_db)):
   user_db = db.query(User).filter(User.email == user.email).first() 
   if not user_db:
       raise HTTPException(400,'Người dùng với email này không tồn tại!')
   # Dòng sau đây đã bị xóa vì không cần thiết và gây hiểu lầm:
   # hash_pw = bcrypt.hashpw(user.password.encode(),bcrypt.gensalt()) 
   is_match = bcrypt.checkpw(user.password.encode(), user_db.password)
   if not is_match:
       raise HTTPException(400,'Mật khẩu không đúng!')
   return user_db