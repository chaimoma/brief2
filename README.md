# Projet : Prédiction du Temps de Livraison

## Contexte et Objectif

Dans ce projet, j'ai été embauchée en tant que data scientist junior par une entreprise de logistique et de livraison.
Mon objectif était de développer un modèle de Machine Learning capable de prédire le temps total d’une livraison, depuis la commande jusqu’à la réception, afin de :

* Anticiper les retards
* Informer les clients en temps réel
* Optimiser l’organisation des tournées

---

## Données et Prétraitement

J'ai travaillé avec un dataset comprenant 1000 commandes et 9 colonnes, incluant la distance, le trafic, le type de véhicule, l’heure de la journée, l’expérience du livreur, la météo et le temps de préparation.

J'ai réalisé :

* Le nettoyage des données en comblant les valeurs manquantes par la médiane pour les colonnes numériques et par le mode pour les colonnes catégorielles.
* L’exploration des données (EDA) pour analyser la distribution et la corrélation des variables.
* La visualisation à l’aide de heatmaps, countplots et boxplots pour identifier les variables les plus importantes.

---

## Modélisation et Sélection du Modèle

J'ai testé deux modèles de régression : **RandomForestRegressor** et **SVR**.
J’ai utilisé GridSearchCV pour optimiser les hyperparamètres et sélectionner le meilleur modèle selon la métrique **MAE (Mean Absolute Error)**.

Après évaluation :

* RandomForest : MAE = 7.27, R² = 0.756
* SVR : MAE = 5.91, R² = 0.817 ✅

Le **SVR** a été choisi comme meilleur modèle pour sa précision et sa capacité à mieux prédire les temps de livraison.

---

## Tests Automatisés

Pour garantir la qualité du code et la reproductibilité :

* J’ai vérifié que le dataset nettoyé avait bien la forme attendue `(1000, 9)`.
* J’ai contrôlé que la MAE du meilleur modèle ne dépassait pas la valeur définie.
  Ces tests sont exécutés automatiquement grâce à **GitHub Actions** à chaque push.

---

## Outils et Technologies Utilisés

* **Python** pour la manipulation de données et la modélisation
* **Pandas, Seaborn, Matplotlib, Scikit-learn** pour l’analyse et le Machine Learning
* **Jupyter Notebook** pour documenter et visualiser les étapes du projet
* **Git et GitHub** pour le versioning et l’intégration continue
* **Jira** pour la gestion et le suivi du projet
* **GitHub Actions** pour automatiser les tests

---

## Résultats et Livrables

* Dataset nettoyé et exploré
* Meilleur modèle : SVR avec MAE = 5.91 et R² = 0.817
* Tests unitaires automatisés réussis
* Workflow GitHub Actions configuré pour exécuter les tests à chaque push
* Documentation et notebooks organisés et reproductibles

---

## Remarques finales

Ce projet m’a permis de mettre en pratique :

* La planification et l’organisation d’un projet ML individuel
* L’exploration de données et la sélection des features
* L’entraînement, l’évaluation et l’optimisation des modèles
* La gestion du code avec GitHub et Jira
* L’automatisation et la reproductibilité via les tests unitaires et GitHub Actions

---