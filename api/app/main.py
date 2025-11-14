from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
import sys
import os

# Ajoutez le chemin pour les imports
sys.path.append(os.path.dirname(__file__))

# Import direct
from services.n8n_client import N8NClient

app = FastAPI(title="Nutrition API")

# Modèles de données
class PatientData(BaseModel):
    age: int
    weight: float
    height: float
    medical_conditions: str = "Aucune"
    allergies: str = "Aucune"
    calorie_target: int = 2000

class DietRequest(BaseModel):
    patient_data: PatientData
    available_ingredients: List[str]

@app.get("/")
def read_root():
    return {"message": "🎉 API Nutrition fonctionne!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/test-n8n")
async def test_n8n():
    """Teste la connexion à n8n"""
    client = N8NClient()
    
    test_data = {
        "age": 35,
        "weight": 70,
        "height": 175,
        "medical_conditions": "Aucune",
        "allergies": "Aucune",
        "calorie_target": 2000
    }
    ingredients = ["poulet", "riz", "oeufs", "légumes", "tomates", "fromage"]
    
    try:
        result = await client.generate_diet_suggestions(test_data, ingredients)
        return {
            "status": "success", 
            "message": "✅ n8n fonctionne correctement",
            "data": result
        }
    except Exception as e:
        return {
            "status": "error", 
            "message": f"❌ Erreur n8n: {str(e)}"
        }

@app.post("/generate-diet")
async def generate_diet(request: DietRequest):
    """Génère un plan alimentaire personnalisé"""
    client = N8NClient()
    
    try:
        result = await client.generate_diet_suggestions(
            request.patient_data.dict(),
            request.available_ingredients
        )
        return {
            "status": "success",
            "message": "📋 Plan alimentaire généré avec succès",
            "data": result
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Erreur lors de la génération: {str(e)}"
        }

@app.get("/patient-info")
def get_patient_info():
    """Retourne des informations sur les données patient attendues"""
    return {
        "patient_data_structure": {
            "age": "int",
            "weight": "float (kg)",
            "height": "float (cm)", 
            "medical_conditions": "string (optionnel)",
            "allergies": "string (optionnel)",
            "calorie_target": "int (optionnel, défaut: 2000)"
        },
        "example_request": {
            "patient_data": {
                "age": 35,
                "weight": 70,
                "height": 175,
                "medical_conditions": "Diabète",
                "allergies": "Aucune",
                "calorie_target": 1800
            },
            "available_ingredients": ["poulet", "riz", "légumes", "oeufs"]
        }
    }