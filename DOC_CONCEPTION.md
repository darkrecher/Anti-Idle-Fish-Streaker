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

 	- Sinon, parcours horizontal de la ligne comportant le pixel turquoise. afin de déterminer la largeur de la `fish_line`. Il s'agit de la ligne en haut du trapèze, sur laquelle se trouve la pointe supérieur du triangle qui passe.
 	
 - les variables `y_line, x1_line, x2_line` permettent de repérer la `fish_line` sur l'écran.

 - Instanciation d'une classe `FishLineAnalyzer` (effectue des copies d'écran de la `fish_line` et les analyse), et d'une classe `FishSubLineAnalyzer` (effectue des copies d'écran d'une ligne située 5 pixels en dessous de la `fish_line`).

 - L'instance de `FishSubLineAnalyzer` est transmise à `FishLineAnalyzer`. Voir plus loin pour la raison à ça.

 -WIP    