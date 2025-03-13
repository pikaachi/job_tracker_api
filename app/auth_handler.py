from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from app.schemas import TokenData
from app.database import get_db  #Use get_db function
from app.models import User

load_dotenv()

# JWT Config
SECRET_KEY = os.getenv("SECRET_KEY")  # Ensure this is set in .env
ALGORITHM = os.getenv("ALGORITHM")  # Ensure this is set in .env

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Extract and authenticate user from JWT token using username instead of user ID."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Decode JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")  # Extract `username` 
        
        if username is None:
            raise credentials_exception

        #print(f" Extracted Username: {username}")  # Debugging log

    except JWTError:
        raise credentials_exception

    # Query the database by username
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception

    return user
