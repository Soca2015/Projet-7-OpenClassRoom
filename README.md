# Parcours Data Science  Projet n°7: "Implémentez un modéle de scoring"

## Description du projet

L'ENTREPRISE "PRÊT À DÉPENSER"
propose des crédits à la consommation pour des personnes ayant peu ou pas du tout d'historique de prêt.
L’entreprise souhaite développer un modèle de Scoring de la probabilité de défaut de paiement du client
pour étayer la décision d'accorder ou non un prêt
Pour réaliser cette étude on s'appuie sur des sources de données variées (données comportementales,
données provenant d'autres institutions financières, etc.).
On doit fournir un outil de compréhension et d'explication du résultat car les clients sont de plus en plus
demandeurs de transparence vis-à-vis des décisions d’octroi de crédit .
Pour cela nous allons mettre en place un dashboard interactif pour que les chargés de relation client
puissent à la fois expliquer de façon la plus transparente possible les décisions d’octroi de crédit, mais
également permettre à leurs clients de disposer de leurs informations personnelles et de les explorer
facilement. 

## Tâches effectuées
    Construire un modèle de scoring qui donnera une prédiction sur la probabilité de faillite d'un client de façon automatique.
    Construire un dashboard interactif à destination des gestionnaires de la relation client permettant d'interpréter les prédictions faites par le modèle et d’améliorer la connaissance client des chargés de relation client.
    Création d'un modéle d'interprétabilité en utilisant LIME
    Création d'une API via Flask et son déploiement en utilisant Heroku
    Création d'un tableau de bord en utilisant Streamlit
    Utilisation de github desktop pour le versionning
Spécifications du dashboard

    Permettre de visualiser le score et l’interprétation de ce score pour chaque client de façon intelligible pour une personne non experte en data science.
    Permettre de visualiser des informations descriptives relatives à un client (via un système de filtre).
    Permettre de comparer les informations descriptives relatives à un client à l’ensemble des clients ou à un groupe de clients similaires.


## Compétences évaluées

-Présenter son travail de modélisation à l'oral
-Déployer un modèle via une API dans le Web
-Utiliser un logiciel de version de code pour assurer l’intégration du modèle
-Rédiger une note méthodologique afin de communiquer sa démarche de modélisation
-Réaliser un dashboard pour présenter son travail de modélisation

## Données

 https://www.kaggle.com/c/home-credit-default-risk/data

## Lien pour l'API
Ceci est notre lien du déploiement de notre API, vous trouverez la table Identifiant qui contient tous les identifiants des clients, vous pouvez rentrer un identifiant de client pour regarder sa probabilité ainsi que son résultat.

https://pret-depenser.herokuapp.com/ 

## Lien pour le Dashboard

https://share.streamlit.io/soca2015/dashboard/dashboard.py

Ceci est le lien de notre dashboard qui contient le résultat de scoring d'un client ainsi que l'intréprétabilité du résultat de scoring.
Il permet de visualiser l'ensemble des attributs d'un client et de tous les clients.

