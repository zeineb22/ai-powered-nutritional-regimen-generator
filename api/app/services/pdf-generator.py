from weasyprint import HTML
from datetime import datetime
import os
from typing import Dict

class PDFGenerator:
    def generate_diet_pdf(self, diet_plan: Dict, patient_info: Dict) -> str:
        """Génère un PDF professionnel du plan alimentaire"""
        
        html_content = self._create_html_template(diet_plan, patient_info)
        
        # Générer nom de fichier unique
        filename = f"diet_plan_{patient_info['id']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        filepath = f"generated_pdfs/{filename}"
        
        # Créer dossier si inexistant
        os.makedirs("generated_pdfs", exist_ok=True)
        
        # Générer PDF
        HTML(string=html_content).write_pdf(filepath)
        
        return filepath
    
    def _create_html_template(self, diet_plan: Dict, patient_info: Dict) -> str:
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Plan Alimentaire - {patient_info['first_name']} {patient_info['last_name']}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                .header {{ text-align: center; border-bottom: 2px solid #333; padding-bottom: 20px; }}
                .patient-info {{ margin: 20px 0; }}
                .day-plan {{ margin: 30px 0; border: 1px solid #ddd; padding: 15px; }}
                .meal {{ margin: 10px 0; padding: 10px; background: #f9f9f9; }}
                .macros {{ color: #666; font-size: 0.9em; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Plan Alimentaire Personnalisé</h1>
                <p>Généré le {datetime.now().strftime('%d/%m/%Y')}</p>
            </div>
            
            <div class="patient-info">
                <h2>Patient</h2>
                <p><strong>Nom:</strong> {patient_info['first_name']} {patient_info['last_name']}</p>
                <p><strong>Âge:</strong> {patient_info.get('age', 'N/A')} ans</p>
                <p><strong>Poids/Taille:</strong> {patient_info['weight']}kg / {patient_info['height']}cm</p>
                <p><strong>Objectif calories:</strong> {diet_plan.get('total_calories', 0)} kcal/jour</p>
            </div>
            
            <div class="diet-plan">
                <h2>Plan Hebdomadaire</h2>
                <!-- Dynamically generate days and meals -->
                {self._generate_days_html(diet_plan)}
            </div>
        </body>
        </html>
        """
    
    def _generate_days_html(self, diet_plan: Dict) -> str:
        # Générer le contenu dynamique des jours
        return "<!-- Plan details -->"