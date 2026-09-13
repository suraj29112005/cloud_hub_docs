from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
class UserResponse(BaseModel):
    id: str
    email: EmailStr
    full_name: str
    role: str
    created_at: datetime
    class Config:
        from_attributes = True
class Token(BaseModel):
    access_token: str
    token_type: str
class IncidentCreate(BaseModel):
    title: str
    description: Optional[str] = None
    severity: str
    service_name: str
class IncidentResponse(BaseModel):
    id: str
    incident_code: str
    title: str
    description: Optional[str]
    severity: str
    status: str
    service_name: str
    created_at: datetime
    class Config:
        from_attributes = True
