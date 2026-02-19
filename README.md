# 🚀 Analyseur de Profils IA (FastAPI + Groq)

Ce projet est une API innovante conçue pour automatiser l'analyse de CV et de profils professionnels en utilisant la puissance de Llama-3 via Groq.

## 📋 Présentation du Concept

### À quoi sert l'application ?
L'application permet d'extraire instantanément les compétences clés, le niveau d'expérience et la pertinence d'un profil par rapport à une fiche de poste. Elle transforme un texte brut (CV) en données structurées exploitables.

### Quel problème elle résout ?
Les recruteurs perdent des heures à trier manuellement des centaines de candidatures. Cette API permet un **pré-filtrage intelligent** et objectif, réduisant le temps de traitement de 80%.

### Qui sont les utilisateurs ?
* **Recruteurs & RH** : Pour gagner du temps sur le sourcing.
* **Agences de placement** : Pour catégoriser rapidement leur base de données.
* **Candidats** : Pour tester l'optimisation de leur CV face à une IA.

---

## 🛠️ Stack Technique
* **Framework** : FastAPI (Python)
* **IA** : Groq Cloud API (Modèle Llama-3-8b)
* **Validation** : Pydantic
* **Serveur** : Uvicorn

## Installation

1. Installez les dépendances : `pip install fastapi groq pydantic`

2. Lancez l'API : `uvicorn cv_api:app --reload`
