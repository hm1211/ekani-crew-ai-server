from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from config.database import Base


class ConsultMessageModel(Base):
    """상담 메시지 ORM 모델"""

    __tablename__ = "consult_messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(36), ForeignKey("consult_sessions.id"), nullable=False, index=True)
    role = Column(String(20), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)

    # Relationships
    session = relationship("ConsultSessionModel", back_populates="messages")