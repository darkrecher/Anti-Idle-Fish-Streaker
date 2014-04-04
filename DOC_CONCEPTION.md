# Document de conception #

## Trucs réutilisables pour d'autres scripts ##

 - `my_logging.py` : config à l'arrache de la librairie logging. En tout cas, ça écrit des accents sur la sortie standard sans se faire chier avec l'encodage.

 - `colrtool.py` : conversion de couleurs RGB -> HSV.

 - `screen_shotter.py` : capture de l'écran (tout, ou une zone spécifique), enregistrement en bmp, récupération des pixels. Il manque juste un peu de doc.

 - `fish_line_detector.find_first_color` : fonction parcourant une ligne ou une colonne d'une capture d'écran, et s'arrête dès le premier pixel correspondant / ne correspondant pas à une tâche spécifique.

## Déroulement global des actions ##

 - Fonction `fish_line_detector.detect` :

 	- Parcours de la colonne de pixel x=900. Détection du premier pixel turquoise corresondant exactement à la couleur de la zone de pêche.

	- Si rien trouvé, on quitte la fonction. Et le script se termine avec l'exception "impossible de trouver la ligne de fishing à l'écran".

 	- Sinon, parcours horizontal de la ligne comportant le pixel turquoise. afin de déterminer où commence et finit la `fish_line`. Il s'agit de la ligne en haut du trapèze, sur laquelle se trouve la pointe supérieur du triangle qui passe.

 - les variables `y_line, x1_line, x2_line` permettent de repérer la `fish_line` sur l'écran.

 - Instanciation d'une classe `FishLineAnalyzer` (effectue des copies d'écran de la `fish_line` et les analyse), et d'une classe `FishSubLineAnalyzer` (effectue des copies d'écran d'une ligne située 5 pixels en dessous de la `fish_line`).

 - L'instance de `FishSubLineAnalyzer` est transmise à `FishLineAnalyzer`. Voir plus loin pour la raison à ça.

 - Instanciation d'une classe `KeyPresser` : classe utilisant la librairie pywin32, capable d'envoyer des touches.

 - La classe `KeyPresser` met le focus sur l'application "Firefox". (C'est pour ça que le script ne marche qu'avec Firefox, en fait il suffirait de changer le nom de l'application dans la classe.

 - Démarrage d'une boucle infinie.

 - Exécution de la fonction `fish_line_analyzer.analyze` :

	 - Fonction `_make_screenshot_main_line` : screenshot de la `fish_line` (zone de 1 pixel de hauteur).

	 - Fonction `_reset_screenshot_values` et `_process_screenshot` : Mise à jour des variables internes :

		 - `x_red_mark_1`, `x_red_mark_2` : positions de la marque rouge représentant la "zone critique" (zone dans laquelle doit se trouver le triangle, au moment où on appuie sur une touche, pour réussir un perfect catch). La marque rouge fait deux pixels de large, c'est pour ça qu'il y a deux variables. Elles peuvent être toutes les deux égales à None lorsque la marque rouge n'est pas présente. De plus, la marque rouge est parfois présente, mais non détectée : lorsque le triangle est proche de la marque rouge, les couleurs se mélangent.

         - `x_triangle` : position de la pointe du triangle sur la `fish_line`.Peut être None lorsqu'aucun triangle n'est présent. À priori, lorsqu'il est présent, on parvient toujours à le détecter, grâce à des approximations sur les couleurs.

         -