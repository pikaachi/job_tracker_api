from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, models, database, utils

router = APIRouter(prefix="/auth", tags=["Authentication"]) 

@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = utils.hash_password(user.password)
    print("Creating user:", user.username)
    print("Hashed password:", hashed_password)
    new_user = models.User(username=user.username, hashed_password=hashed_password)


    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
