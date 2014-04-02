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

C'est du "chez moi ça marche". Donc aucune garantie de fonctionnement, et certainement aucune garantie de simplicité.

Ne fonctionne que sous Windows.

Ne fonctionne qu'avec Firefox (pour une raison stupide et très facilement corrigeable, mais c'est ainsi).

 - Installer python 2.6.6 ou supérieur. Pas le python 3, qui n'est pas rétro-compatible avec les 2.x.
 - Installer la librairie wxPython. Je ne sais plus exactement où ça se trouve. Mais c'est pas très compliqué. Personnellement, j'ai la version "2.8.12.1 (msw-unicode)"
 - Installer la librairie pywin32. Pareil, je sais plus exactement où elle est. Personnellement, le nom du fichier d'installation que j'ai utilisé est "pywin32-218.win32-py2.6.exe"

WIP

 - Positionner l'écran de jeu. colonne 900. si y'a du cyan qui fait pas partie de la ligne de fishing, y'aura plantage silencieux.
 - Bien vérifier que dans la fenêtre de Firefox, c'est le flash qui a le focus. Fermer les autres fenêtres Firefox. 
 - Attendre qu'un triangle passe. Faut pas que ce soit en vert/rouge
 - Ouvrir une console MS-DOS et lancer le script
 - Si ça pète avec l'exception "impossible de trouver la ligne de fishing", repositionner éventuelleement, et relancer.
 - Le focus va changer.
 - Ne rien toucher !
 - Ça va logger des trucs dans la console. 
 - Si des fenêtres de milestone. les fermer.
 - Surtout ne pas changer d'appli.
 - Aller dans la fenêtre de console et appuyer sur Ctrl-C.

# Doc de conception #

WIP aussi. Mais ce sera assez court.

# Crédits #

Créé par Réchèr. 

Le code et cette doc sont sous la double licence : Art Libre ou Creative Commons CC-BY (au choix).

Repository : https://github.com/darkrecher/Anti-Idle-Fish-Streaker

Mon blog : http://recher.wordpress.com