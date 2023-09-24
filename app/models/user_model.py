from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from app.database.settings import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime ,default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"[User: {self.username} | Email: {self.email}]"

