"""
Route definitions for the GameList API.

See README for the suggested build order. Route bodies below are TODO;
each docstring describes the expected behavior — implement them using the
helpers in app/auth.py.
"""

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import Token, UserCreate, UserLogin, UserOut

app = FastAPI(title="GameList")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Resolve the current user from the access token on the request.

    Expected behavior:
    - Decode the token (app.auth.decode_token); on failure, raise a 401.
    - Look up the user identified by the token's claims in the DB.
    - If no such user exists, raise a 401.
    - Otherwise return the User model instance so route handlers can use it.
    """
    # TODO: implement
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not implemented")


@app.post("/auth/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user.

    Expected behavior:
    - Reject if a user with this email already exists (409 Conflict).
    - Hash the password (app.auth.hash_password) — never store it plaintext.
    - Create and commit the new User row.
    - Return the created user (without the password).
    """
    # TODO: implement
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@app.post("/auth/login", response_model=Token)
def login(payload: UserLogin, db: Session = Depends(get_db)):
    """
    Authenticate a user and issue tokens.

    Expected behavior:
    - Look up the user by email; if not found, raise 401.
    - Verify the password against the stored hash (app.auth.verify_password);
      if it doesn't match, raise 401.
    - Issue an access token (app.auth.create_access_token) and return it.
    - Once the RefreshToken model exists, also issue + store a refresh
      token and set it as an httpOnly, SameSite=Strict cookie (see the
      README's notes on the security decisions baked into this scaffold).
    """
    # TODO: implement
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@app.get("/auth/me", response_model=UserOut)
def get_me(current_user=Depends(get_current_user)):
    """
    Return the currently authenticated user.

    Your first protected route — exercises get_current_user end-to-end.
    """
    return current_user
