from sqlalchemy import Column, String, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class ConsultSessionModel(Base):
    """상담 세션 ORM 모델"""

    __tablename__ = "consult_sessions"

    id = Column(String(36), primary_key=True)
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False, index=True)
    mbti = Column(String(4), nullable=False)  # 상담 시작 시점 스냅샷
    gender = Column(String(10), nullable=False)  # 상담 시작 시점 스냅샷
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    is_completed = Column(Boolean, default=False, nullable=False)
    analysis_json = Column(Text, nullable=True)  # JSON 형태로 분석 결과 저장

    # Relationships
    user = relationship("UserModel", back_populates="consult_sessions")
    messages = relationship("ConsultMessageModel", back_populates="session")
