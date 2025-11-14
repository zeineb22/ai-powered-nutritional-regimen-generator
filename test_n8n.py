import asyncio
import httpx
import json

async def test_n8n_direct():
    """Test direct de n8n sans classes complexes"""
    print("🚀 Test direct de n8n...")
    
    # Données de test
    test_data = {
        "prompt": "Générer un plan alimentaire pour patient diabétique",
        "patient_data": {
            "age": 35,
            "weight": 68,
            "height": 170,
            "medical_conditions": "Diabète",
            "allergies": "Aucune",
            "calorie_target": 1800
        },
        "available_ingredients": ["poulet", "riz", "brocoli", "carottes", "oeufs"],
        "requirements": {
            "output_format": "json",
            "max_recipes_per_day": 4,
            "use_available_ingredients": True
        }
    }
    
    try:
        print("📤 Envoi de la requête à n8n...")
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:5678/webhook-test/webhook/diet-generation",
                json=test_data,
                timeout=30.0
            )
            
            if response.status_code == 200:
                result = response.json()
                print("✅ Succès! Réponse reçue:")
                print(json.dumps(result, indent=2, ensure_ascii=False))
                return True
            else:
                print(f"❌ Erreur HTTP: {response.status_code} - {response.text}")
                return False
                
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

if __name__ == "__main__":
    asyncio.run(test_n8n_direct())