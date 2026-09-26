"""
Password hashing and JWT helpers.

TODO: implement each function below. Suggested build order (see README):
1. hash_password / verify_password — test in isolation first.
2. create_access_token / decode_token — encode something, decode it back,
   and confirm you get the original data out, before wiring up any routes.
3. create_refresh_token — same idea as access tokens, just longer-lived.
"""

from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "CHANGE_ME"  # TODO: load from an environment variable before deploying
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str) -> str:
    """Hash a plaintext password with Argon2."""
    # TODO: implement using pwd_context.hash
    raise NotImplementedError


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check a plaintext password against a stored Argon2 hash."""
    # TODO: implement using pwd_context.verify
    raise NotImplementedError


def create_access_token(data: dict) -> str:
    """
    Create a short-lived JWT access token.

    `data` should carry whatever claims routes need (at minimum something
    identifying the user, e.g. {"sub": user.email}). Expires after
    ACCESS_TOKEN_EXPIRE_MINUTES.
    """
    # TODO: copy data, add an "exp" claim, encode with jwt.encode
    raise NotImplementedError


def create_refresh_token(data: dict) -> str:
    """
    Create a longer-lived JWT refresh token.

    Same idea as create_access_token, but expires after
    REFRESH_TOKEN_EXPIRE_DAYS. Only wire this in once basic
    register/login/me works end-to-end (see README).
    """
    # TODO: implement
    raise NotImplementedError


def decode_token(token: str) -> dict:
    """
    Decode and verify a JWT, returning its payload.

    Should let jose.JWTError propagate (or raise your own error) if the
    token is expired, malformed, or has a bad signature — callers rely on
    that to reject invalid tokens.
    """
    # TODO: implement using jwt.decode
    raise NotImplementedError
