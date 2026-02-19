# Analyseur de Profils FastAPI (Groq & Llama-3)

## Note sur le choix technologique
Pour ce projet, j'ai choisi d'utiliser l'IA de **Groq** à la place d'OpenAI pour les raisons suivantes :
* **Accessibilité** : OpenAI est désormais payant dès la première utilisation, ce qui bloquait l'exécution à cause des quotas.
* **Performance** : Groq offre un accès ultra-rapide au modèle **Llama-3**.
* **Gratuité** : Ce choix permet de présenter un projet totalement fonctionnel, gratuit et performant.

## Installation
1. Installez les dépendances : `pip install fastapi groq pydantic`
2. Lancez l'API : `uvicorn cv_api:app --reload`
