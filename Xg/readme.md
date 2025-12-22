# Expected Goals (xG) Model

## 📌 Description
Ce projet a pour objectif de calculer l’**Expected Goals (xG)** à partir de données de football contenues dans des fichiers **CSV**.  
Le modèle est basé sur un algorithme de **machine learning (XGBoost)** afin d’estimer la probabilité qu’un tir aboutisse à un but.

Ce dépôt est conçu pour être facilement extensible et maintenable.

---

## 📂 Structure du projet

```text
project_root/
│
├── README.md
├── requirements.txt
│
├── data/          # Chargement et preprocessing des données
├── models/        # Entraînement et évaluation du modèle XGBoost
│
└── notebooks/         # Analyses et expérimentations
