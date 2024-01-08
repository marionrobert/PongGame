<h1>Pong Game</h1>
Ce projet consiste en un jeu Pong développé en Python utilisant le module Turtle pour la création de l'interface graphique.

<h2>Présentation du jeu</h2>
Le jeu Pong est un jeu classique où deux joueurs contrôlent des raquettes pour frapper une balle et marquer des points. Le joueur qui atteint un score prédéfini remporte la partie.

<h2>Contenu du projet</h2>
Fichiers inclus :
<ul>
  <li>main.py: Le fichier principal du jeu qui initialise l'interface graphique, crée les éléments du jeu (paddles, balle, score) et gère la logique du jeu.</li>
  <li>scoreboard.py: Ce fichier définit la classe Scoreboard pour afficher et mettre à jour les scores des joueurs ainsi que le message de fin de partie.</li>
  <li>ball.py: Le fichier contenant la classe Ball qui représente la balle du jeu et définit ses mouvements et rebonds.</li>
  <li>paddle.py: Ce fichier contient la classe Paddle qui définit les raquettes des joueurs et leurs déplacements.</li>
</ul>

<h2>Comment jouer ?</h2>
Exécutez le fichier main.py pour démarrer le jeu.
Les joueurs contrôlent les raquettes avec les touches suivantes :
<ul>
  <li>Joueur 1 (droite) : Flèches haut et bas.</li>
  <li>Joueur 2 (gauche) : Touches "z" et "q".</li>
</ul>

Vous pouvez modifier les touches de commande en modifiant les lignes suivantes : 
<img src="/assets/screenshot_code.png" />

Le jeu se poursuit jusqu'à ce qu'un joueur atteigne le score gagnant, moment où le jeu se termine et affiche le vainqueur.
Le score gagnant est initialisé à 6 mais vous pouvez modifer cette variable (winning_score).

<h2>Apperçu de l'interface</h2>
<img src="/assets/screenshot_ponggame.png" />

<h2>Remarques</h2>
Projet réalisé dans le cadre du cours <a href="https://www.udemy.com/course/100-days-of-code/">100 Days of Code: The Complete Python Pro Bootcamp</a> de Angela Yu sur la plateform Udemy.
