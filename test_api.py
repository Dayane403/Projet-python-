from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
import json

app = FastAPI()

# Ton client Groq bien configuré
client = Groq(api_key="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")


class TranslateRequest(BaseModel):
    message: str
    target_language: str


@app.post("/translate")
def translate(data: TranslateRequest):
    prompt = f"Traduis le message suivant en {data.target_language} : {data.message}"

    try:
        # Utilisation de la syntaxe correcte pour Groq
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Modèle gratuit et rapide de Groq
            messages=[
                {"role": "system", "content": "Tu es un traducteur professionnel."},
                {"role": "user", "content": prompt}
            ]
        )

        # On récupère le texte avec la syntaxe pointée (.)
        translated_text = response.choices[0].message.content

        return {
            "original": data.message,
            "translated": translated_text,
            "language": data.target_language
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))