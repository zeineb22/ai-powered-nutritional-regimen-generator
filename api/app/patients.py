from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models import Patient
from schemas import PatientCreate, Patient

router = APIRouter()

@router.post("/patients/", response_model=Patient)
def create_patient(patient: PatientCreate, session: Session = Depends(get_session)):
    db_patient = Patient(**patient.dict())
    session.add(db_patient)
    session.commit()
    session.refresh(db_patient)
    return db_patient

@router.get("/patients/", response_model=list[Patient])
def read_patients(session: Session = Depends(get_session)):
    patients = session.exec(select(Patient)).all()
    return patients

@router.get("/patients/{patient_id}", response_model=Patient)
def read_patient(patient_id: int, session: Session = Depends(get_session)):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient