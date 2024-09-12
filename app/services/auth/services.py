from sqlalchemy.orm import Session
from app.models import user
from app.schemas.user_schema import UserRegister

def get_user_by_name(db: Session, username: str):
    return db.query(user.User).filter(user.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(user.User).filter(user.User.email == email).first()

def get_user_by_id(db: Session, id: int):
    return db.query(user.User).filter(user.User.id == id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user.User).offset(skip).limit(limit).all()

def create_user(db: Session, user:UserRegister):
    db_user = user.User(username=user.username, email=user.email, password = user.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: UserRegister, id: int):
    db_user = db.query(user.User).filter(user.User.id == id).first()
    db_user.username = user.username
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, id: int):
    db_user = db.query(user.User).filter(user.User.id == id).first()
    db.delete(db_user)
    db.commit()
    return db_user
