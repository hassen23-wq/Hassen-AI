from google import genai
from config import GEMINI_API_KEY

# 1. Initialisation mta3 el Client
client = genai.Client(api_key=GEMINI_API_KEY)

print("=== LISTE DES MODÈLES GEMINI DISPONIBLES ===")

# 2. Récupération w affichage mta3 les modèles
try:
    for model in client.models.list():
        # Ne garder que les modèles de génération de texte/chat
        if "generateContent" in model.supported_actions:
            print(f"• Nom du modèle : {model.name}")
except Exception as e:
    print(f"Erreur lors de la récupération des modèles : {e}")