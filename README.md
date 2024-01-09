# Pong Game

Ce projet consiste en un jeu Pong développé en Python utilisant le module Turtle et la programmation orientée objet.

## Présentation du jeu

Le jeu Pong est un jeu classique où deux joueurs contrôlent des raquettes pour frapper une balle et marquer des points. Le joueur qui atteint un score prédéfini remporte la partie.

## Contenu du projet

### Fichiers inclus :

- `main.py`: Le fichier principal du jeu qui initialise l'interface graphique, crée les éléments du jeu (paddles, balle, score) et gère la logique du jeu.
- `scoreboard.py`: Ce fichier définit la classe Scoreboard pour afficher et mettre à jour les scores des joueurs ainsi que le message de fin de partie.
- `ball.py`: Le fichier contenant la classe Ball qui représente la balle du jeu et définit ses mouvements et rebonds.
- `paddle.py`: Ce fichier contient la classe Paddle qui définit les raquettes des joueurs et leurs déplacements.

## Comment jouer ?

Exécutez le fichier `main.py` pour démarrer le jeu.
Les joueurs contrôlent les raquettes avec les touches suivantes :
- Joueur 1 (droite) : Flèches haut et bas.
- Joueur 2 (gauche) : Touches "z" et "q".

Vous pouvez modifier les touches de commande en modifiant les lignes suivantes : 
![Code Screenshot](/assets/screenshot_code.png)

Le jeu se poursuit jusqu'à ce qu'un joueur atteigne le score gagnant, moment où le jeu se termine et affiche le vainqueur.
Le score gagnant est initialisé à 6 mais vous pouvez modifier cette variable (winning_score).

## Apperçu de l'interface

![Game Screenshot](/assets/screenshot_ponggame.png)

## Remarques

Projet réalisé dans le cadre du cours [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) de Angela Yu sur la plateforme Udemy.
