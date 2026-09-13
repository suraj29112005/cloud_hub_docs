import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
class User(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=False)
    role = Column(String(32), default="responder")
    created_at = Column(DateTime, default=datetime.utcnow)
class Incident(Base):
    __tablename__ = "incidents"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    incident_code = Column(String(32), unique=True, index=True, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    severity = Column(String(16), nullable=False)
    status = Column(String(32), default="triggered")
    service_name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    timeline_events = relationship("TimelineEvent", back_populates="incident", cascade="all, delete-orphan")
class TimelineEvent(Base):
    __tablename__ = "timeline_events"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    incident_id = Column(String(36), ForeignKey("incidents.id", ondelete="CASCADE"), nullable=False)
    author = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    incident = relationship("Incident", back_populates="timeline_events")
