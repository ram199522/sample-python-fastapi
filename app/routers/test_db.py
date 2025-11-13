from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, User  # your SQLAlchemy session and User model
from pydantic import BaseModel

router = APIRouter(tags=["users"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for input
class UserCreate(BaseModel):
    name: str

# Endpoint to add a new user
@router.post("/add-user/")
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=user.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "name": new_user.name}

# Endpoint to fetch the first user
@router.get("/test-db/")
def test_db(db: Session = Depends(get_db)):
    user = db.query(User).first()
    return {"user": user.name if user else "No users found"}

# Endpoint to fetch all users
@router.get("/all-users/")
def all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {"users": [user.name for user in users]}
