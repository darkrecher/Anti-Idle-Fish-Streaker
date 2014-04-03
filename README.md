# Anti-Idle Fish Streaker #

Un script pour faire des streaks au sous-jeu "Fishing", du jeu flash Anti-Idle, jouable sur Kongregate. (http://www.kongregate.com/games/Tukkun/anti-idle-the-game)

Ça ne fonctionne pas à 100%, mais c'est tout à fait suffisant pour atteindre le streak de 20, nécessaire à un achievement.

Le jeu Fishing se présente sous cette forme :

![screenshot anti-idle fishing](https://raw.githubusercontent.com/darkrecher/Anti-Idle-Fish-Streaker/master/screenshots/001_fish.png)

Le seul truc intéressant se trouve en bas à droite : le trapèze aux bords turquoise. Le triangle orange qui est dedans se déplace latéralement. Lorsqu'il arrive pil poil au niveau du trait rouge vertical, il faut appuyer sur une touche, ce qui permet de faire un "perfect catch". Puis, un autre triangle passe, et ainsi de suite.

Un "streak" désigne le fait de réussir plusieurs perfect catch à la suite.   

# Principe de fonctionnement #

Le script effectue périodiquement des copies d'écran. Il repère la position du triangle et la zone de perfect catch. Lorsque le triangle est dedans, le script simule un appui de touche qui est envoyé au navigateur web. 

Le script peut continuer ainsi indéfiniment, ce qui permet de faire des streaks assez important.   

# Mode d'emploi #

C'est du "chez moi ça marche". Donc aucune garantie de fonctionnement, et certainement aucune garantie de simplicité d'emploi. Bon courage.

Ne fonctionne que sous Windows.

Ne fonctionne qu'avec Firefox (pour une raison stupide et très facilement corrigeable, mais c'est ainsi).

 - Installer python 2.6.6 ou supérieur. Pas le python 3, qui n'est pas rétro-compatible avec les 2.x.

 - Installer la librairie wxPython. Dans mes souvenirs, c'est pas très compliqué à faire. Personnellement, j'ai la version "2.8.12.1 (msw-unicode)"

 - Installer la librairie pywin32. Le nom du fichier d'installation que j'ai utilisé est "pywin32-218.win32-py2.6.exe"

 - Télécharger tout ce repository, et placer le tel quel sur le disque dur, n'importe où.

 - Démarrer le jeu dans Firefox. Placer la fenêtre de façon à ce que la "zone de pêche" (le trapèze aux bords turquoise) soit traversée par la colonne de pixels située à x=900. (x=0 : colonne tout à gauche). La position de cette colonne dépend de la résolution de votre écran. Débrouillez-vous avec ça.  

 - Si la zone de pêche n'est pas tout à fait bien placée, et que c'est un bord oblique du trapèze qui se trouve à x=900, le script ne fonctionnera pas. Le truc rigolo, c'est qu'aucun message d'erreur explicite ne sera signalé.

 - Cliquer sur le jeu, afin d'être sûr que c'est lui qui reprendra le focus lors de l'activation de la fenêtre de Firefox. Ne pas ouvrir d'autres fenêtres Firefox. 

 - Ouvrir une console MS-DOS. Se placer dans le répertoire contenant le repository téléchargé.

 - Vérifier que même la zone de pêche est entièrement visible à l'écran.

 - Attendre qu'un triangle passe, ou soit en attente de passer. Il ne faut pas que la zone de pêche soit en surbrillance verte ou rouge suite à l'attrapage ou l'échec d'attrapage d'un triangle.

 - dans la console, lancer la commande `c:\python27\python.exe main.py`. (Remplacer `c:\python27\` par le répertoire d'installation de python).

 - Si le script se termine immédiatement, avec l'exception "impossible de trouver la ligne de fishing", il faut le relancer, en ayant éventuellement repositionné la zone de pêche au bon endroit de l'écran.

 - Si tout va bien, la fenêtre de Firefox va automatiquement devenir la fenêtre active.

 - Surtout, ne rien toucher ! Si c'est une autre fenêtre qui devient active pendant que le script tourne, les appuis de touche risquent d'être envoyés ailleurs. 

 - Des infos diverses seront loggées dans la console, au fur et à mesure des captures d'écran, de la détection des triangles, etc.

 - Normalement, les perfect catch devraient s'effectuer tout seul, les uns après les autres.

 - Si le jeu affiche des messages de "milestone", il est possible de les refermer sans interrompre le script. Mais il est conseillé de ne faire aucune autre action.

 - Pour arrêter le script, cliquer sur la console MS-DOS et appuyer sur Ctrl-C. (Assez-vite, sinon la console va s'envoyer des appuis de touche sur elle-même, et c'est un peu bizarre).

# Doc de conception #

WIP. Mais ce sera assez court.

# Crédits #

Créé par Réchèr. 

Le code et cette doc sont sous la double licence : Art Libre ou Creative Commons CC-BY (au choix).

Repository : https://github.com/darkrecher/Anti-Idle-Fish-Streaker

Mon blog : http://recher.wordpress.com