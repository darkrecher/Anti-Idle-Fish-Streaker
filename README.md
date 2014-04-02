# Anti-Idle Fish Streaker #

Un script pour faire des streaks au sous-jeu "Fishing", du jeu Flash "Anti-Idle", jouable sur Kongregate. (http://www.kongregate.com/games/Tukkun/anti-idle-the-game)

Ça ne fonctionne pas à 100%, mais c'est tout à fait suffisant pour atteindre le streak de 20, nécessaire à un achievement.

Le jeu Fishing se présente sous cette forme :

![screenshot anti-idle fishing](https://raw.githubusercontent.com/darkrecher/Anti-Idle-Fish-Streaker/master/screenshots/001_fish.png)

Le seul truc intéressant se trouve en bas à droite : le trapèze aux bords turquoise. Le triangle orange qui est dedans se déplace latéralement. Lorsqu'il arrive pil poil au niveau du trait rouge vertical, il faut appuyer sur une touche, ce qui permet de faire un "perfect catch". Puis, un autre triangle passe, et ainsi de suite.

Lorsqu'on effectue plusieurs perfect catch les uns après les autres, ça s'appelle un "streak". L'un des achievements du jeu demande d'atteindre un streak de 20 perfect catch consécutifs.   

# Principe de fonctionnement #

Le script effectue périodiquement des copies d'écran. Il repère la position du triangle et de la zone de "perfect catch". Lorsque le triangle est dans la zone, le script simule un appui de touche qui est envoyé au navigateur web. Le jeu compte cela comme un perfect catch. 

Le script effectue cette action indéfiniment, ce qui permet de faire des streaks assez important.   

# Mode d'emploi #

C'est du "chez moi ça marche". Donc aucune garantie de fonctionnement, et certainement aucune garantie de simplicité d'emploi. Bon courage.

Ne fonctionne que sous Windows.

Ne fonctionne qu'avec Firefox (pour une raison stupide et très facilement corrigeable, mais c'est ainsi).

 - Installer python 2.6.6 ou supérieur. Pas le python 3, qui n'est pas rétro-compatible avec les 2.x.
 - Installer la librairie wxPython. Je ne sais plus exactement où ça se trouve. Mais c'est pas très compliqué. Personnellement, j'ai la version "2.8.12.1 (msw-unicode)"
 - Installer la librairie pywin32. Pareil, je sais plus exactement où elle est. Personnellement, le nom du fichier d'installation que j'ai utilisé est "pywin32-218.win32-py2.6.exe"
 - Télécharger tout ce repository, et placer le tel quel sur le disque dur, n'importe où.
 - Démarrer le jeu dans Firefox. Placer la fenêtre de façon à ce que la "zone de pêche" (le trapèze aux bords turquoise) soit traversée par la colonne de pixels située à x=900. (x=0 : colonne tout à gauche). La position de cette colonne dépend de la résolution de l'écran. Débrouillez-vous pour la trouver.  
 - Si la zone de pêche n'est pas tout à fait bien placée, et que c'est un bord oblique du trapèze qui se trouve à x=900, le script ne fonctionnera pas. Et en plus, aucun message d'erreur explicite ne sera signalé.
 - Cliquer sur le jeu, afin d'être sur que c'est lui qui reprend le focus lorsqu'on retournera à la fenêtre de Firefox. Ne pas ouvrir d'autres fenêtres Firefox. 
 - Ouvrir une console MS-DOS. Se placer dans le répertoire contenant le repository téléchargé.
 - Vérifier que même si Firefox n'est pas la fenêtre active, aucune autre fenêtre ne recouvre la zone de pêche.
 - Attendre qu'un triangle passe, ou soit en attente de passer. Il ne faut pas que la zone de pêche soit en surbrillance verte ou rouge suite à l'attrapage ou l'échec d'attrapage d'un triangle.
 - dans la console, lancer la commande `c:\python27\python.exe main.py`. (Remplacer `c:\python27\` par le répertoire d'installation de python).
 - Si le script se termine immédiatement, avec un message d'exception "impossible de trouver la ligne de fishing", il faut le relancer, en ayant éventuellement repositionné la fenêtre de Firefox au bon endroit.
 - Si tout va bien, la fenêtre de Firefox va automatiquement devenir la fenêtre active.
 - Surtout, ne rien toucher ! Si on change de fenêtre active pendant que le script tourne, les appuis de touche risquent d'être envoyés à d'autres applications. 
 - Des infos diverses seront loggées dans la console, au fur et à mesur des analyse d'image, de la détection des triangles, etc.
 - Normalement, les perfect catch devraient s'effectuer tout seul, les uns après les autres.
 - Si des indications de "milestone" apparaissent dans le jeu, pendant les perfect catch, il est possible de les refermer. Mais il est conseillé de ne faire aucune autre action.
 - Pour arrêter le script, cliquer dans la console MS-DOS et appuyer sur Ctrl-C. (Assez-vite, sinon la console va s'envoyer des appuis de touche sur elle-même, et c'est un peu bizarre).

# Doc de conception #

WIP. Mais ce sera assez court.

# Crédits #

Créé par Réchèr. 

Le code et cette doc sont sous la double licence : Art Libre ou Creative Commons CC-BY (au choix).

Repository : https://github.com/darkrecher/Anti-Idle-Fish-Streaker

Mon blog : http://recher.wordpress.com