# Anti-Idle Fish Streaker #

Un script pour faire des streaks au sous-jeu "Fishing", du jeu Flash "Anti-Idle", jouable sur Kongregate. (http://www.kongregate.com/games/Tukkun/anti-idle-the-game)

Ça ne fonctionne pas à 100%, mais c'est tout à fait suffisant pour atteindre le streak de 20, nécessaire à un achievement.

Le jeu Fishing se présente sous cette forme :

![screenshot anti-idle fishing](https://raw.githubusercontent.com/darkrecher/Anti-Idle-Fish-Streaker/master/screenshots/001_fish.png)

Le seul truc intéressant se trouve en bas à droite. Le triangle orange se déplace latéralement. Lorsqu'il arrive pil poil au niveau du trait rouge vertical, il faut appuyer sur une touche, ce qui permet de faire un "perfect catch". Puis, un autre triangle passe, et ainsi de suite.

Lorsqu'on effectue plusieurs perfect catch les uns après les autres, ça s'appelle un "streak". L'un des achievements du jeu demande d'atteindre un streak de 20 perfect catch consécutifs.   

# Principe de fonctionnement #

Le script effectue périodiquement des copies d'écran. Il repère la position du triangle et de la zone de "perfect catch". Lorsque le triangle est dans la zone, le script simule un appui de touche qui est envoyé au navigateur web. Le jeu compte cela comme un perfect catch. 

Le script effectue cette action indéfiniment, ce qui permet de faire des streaks assez important.   

# Mode d'emploi #

WIP

# Doc de conception #

WIP aussi. Mais ce sera assez court.

# Crédits #

Créé par Réchèr. 

Le code et cette doc sont sous la double licence : Art Libre ou Creative Commons CC-BY (au choix).

Repository : https://github.com/darkrecher/Anti-Idle-Fish-Streaker

Mon blog : http://recher.wordpress.com