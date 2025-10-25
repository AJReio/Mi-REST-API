from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy import func
from app.database.database import Base


# Modelo de usuario
class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, username={self.username})>"
    
    # Modelo de post
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=True)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, nullable=False)
    is_published = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__ (self):
        return f"<Post(id={self.id}, title={self.title}, author_id={self.author_id})>"