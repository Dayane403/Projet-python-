from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
import json

app = FastAPI()

# Mets ta clé Groq ici (gsk_...)
client = Groq(api_key="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")


class ProfileRequest(BaseModel):
    name: str
    current_skills: list[str]
    experience_years: int
    target_job: str


@app.post("/analyze-profile")
def analyze_profile(data: ProfileRequest):
    prompt = f"Analyse ce profil pour le poste de {data.target_job} : Nom: {data.name}, Compétences: {data.current_skills}. Réponds STRICTEMENT en JSON."

    try:
        # On utilise le modèle Llama-3 qui est gratuit sur Groq
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))