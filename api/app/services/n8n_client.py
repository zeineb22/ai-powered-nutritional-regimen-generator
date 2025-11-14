import httpx
import os
from typing import Dict, Any, List

class N8NClient:
    def __init__(self):
        self.base_url = os.getenv("N8N_URL", "http://localhost:5678")
        self.webhook_path = "/webhook/diet-generation"
    
    async def generate_diet_suggestions(self, patient_data: Dict, available_ingredients: List[str]) -> Dict[str, Any]:
        # CORRECTION : Définir la variable prompt AVANT de l'utiliser
        prompt = f"""
        En tant que nutritionniste expert, génère un plan alimentaire JSON pour:
        - Patient: {patient_data['age']} ans, {patient_data['weight']}kg, {patient_data['height']}cm
        - Conditions: {patient_data.get('medical_conditions', 'Aucune')}
        - Allergies: {patient_data.get('allergies', 'Aucune')}
        - Cible calories: {patient_data.get('calorie_target', 2000)} kcal
        - Ingrédients disponibles: {', '.join(available_ingredients)}
        
        Retourne UNIQUEMENT du JSON valide.
        """
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}{self.webhook_path}",
                json={
                    "prompt": prompt,  # ← Maintenant prompt est défini
                    "patient_data": patient_data,
                    "available_ingredients": available_ingredients,
                    "requirements": {
                        "output_format": "json",
                        "max_recipes_per_day": 4,
                        "use_available_ingredients": True,
                        "ai_enhanced": False
                    }
                },
                timeout=30.0
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"n8n error: {response.status_code} - {response.text}")