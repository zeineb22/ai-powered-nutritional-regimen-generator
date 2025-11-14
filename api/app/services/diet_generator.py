from sqlmodel import Session, select
import pulp
from typing import List, Dict
from models import Patient, Recipe, Ingredient, RecipeIngredient
from schemas import DietGenerationRequest, DietPlanResponse, MealSuggestion
from .n8n_client import N8NClient

class DietGenerator:
    def __init__(self, session: Session):
        self.session = session
        self.n8n_client = N8NClient()
    
    async def generate_weekly_plan(self, patient_id: int, target_calories: float = None, days: int = 7):
        # 1. Récupérer données patient
        patient = self.session.get(Patient, patient_id)
        if not patient:
            raise ValueError("Patient not found")
        
        # 2. Calculer cibles si non fournies
        if not target_calories:
            target_calories = self._calculate_calorie_needs(patient)
        
        # 3. Appeler n8n pour suggestions initiales
        patient_data = {
            "age": self._calculate_age(patient.date_of_birth),
            "weight": patient.weight,
            "height": patient.height,
            "medical_conditions": patient.medical_conditions,
            "allergies": patient.allergies,
            "calorie_target": target_calories
        }
        
        available_ingredients = self._get_available_ingredients()
        ai_suggestions = await self.n8n_client.generate_diet_suggestions(
            patient_data, available_ingredients
        )
        
        # 4. Optimiser avec programmation linéaire
        optimized_plan = self._optimize_with_lp(ai_suggestions, target_calories)
        
        return optimized_plan
    
    def _calculate_calorie_needs(self, patient: Patient) -> float:
        # Formule Harris-Benedict simplifiée
        bmr = 10 * patient.weight + 6.25 * patient.height - 5 * self._calculate_age(patient.date_of_birth)
        return bmr * 1.2  # Facteur activité légère
    
    def _calculate_age(self, birth_date) -> int:
        from datetime import date
        today = date.today()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    def _get_available_ingredients(self) -> List[str]:
        ingredients = self.session.exec(select(Ingredient)).all()
        return [ing.name for ing in ingredients]
    
    def _optimize_with_lp(self, ai_suggestions: Dict, target_calories: float):
        # Implémentation simplifiée de l'optimisation
        # Utilise PuLP pour ajuster les portions et respecter les contraintes
        prob = pulp.LpProblem("Diet_Optimization", pulp.LpMinimize)
        
        # Ici, ajouter les variables et contraintes d'optimisation
        # Retourner le plan optimisé
        return ai_suggestions  # Temporaire