from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from schemas import DietGenerationRequest, DietPlanResponse
from services.diet_generator import DietGenerator

router = APIRouter()

@router.post("/diets/generate", response_model=DietPlanResponse)
def generate_diet_plan(
    request: DietGenerationRequest, 
    session: Session = Depends(get_session)
):
    generator = DietGenerator(session)
    diet_plan = generator.generate_weekly_plan(
        patient_id=request.patient_id,
        target_calories=request.target_calories,
        days=request.days
    )
    return diet_plan