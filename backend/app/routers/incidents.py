import random
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Incident
from app.schemas.schemas import IncidentCreate, IncidentResponse
from app.security import get_current_user
router = APIRouter(prefix="/api/v1/incidents", tags=["Incidents"])
@router.get("", response_model=List[IncidentResponse])
def list_incidents(db: Session = Depends(get_db)):
    return db.query(Incident).all()
@router.post("", response_model=IncidentResponse, status_code=201)
def create_incident(payload: IncidentCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    inc = Incident(incident_code=f"INC-{random.randint(1000, 9999)}", title=payload.title, description=payload.description, severity=payload.severity, service_name=payload.service_name)
    db.add(inc); db.commit(); db.refresh(inc)
    return inc
