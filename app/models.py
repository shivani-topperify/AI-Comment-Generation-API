from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)

    platform = Column(String(50), nullable=False)
    community = Column(String(100), nullable=True)

    post_title = Column(Text, nullable=False)
    post_content = Column(Text, nullable=False)

    generated_comment = Column(Text, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)