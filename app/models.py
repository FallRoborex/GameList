from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


# TODO: RefreshToken model — add once register/login/me work end-to-end.
#
# Should store: the refresh token (or a hash of it), a user_id FK back to
# User, an expires_at, and enough state to revoke/rotate it on login so a
# stolen refresh token can't be reused indefinitely.
