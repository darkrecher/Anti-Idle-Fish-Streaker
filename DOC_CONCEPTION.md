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

 	- Sinon, parcours horizontal de la ligne comportant le pixel turquoise. afin de déterminer où commence et finit la fish_line. Il s'agit de la ligne en haut du trapèze, sur laquelle se trouve la pointe supérieur du triangle qui passe.

 - les variables `y_line, x1_line, x2_line` permettent de repérer la fish_line sur l'écran.

 - Instanciation d'une classe `FishLineAnalyzer` (effectue des copies d'écran de la fish_line et les analyse), et d'une classe `FishSubLineAnalyzer` (effectue des copies d'écran d'une ligne située 5 pixels en dessous de la fish_line).

 - L'instance de `FishSubLineAnalyzer` est transmise à `FishLineAnalyzer`. Voir plus loin pour la raison à ça.

 - Instanciation d'une classe `KeyPresser` : classe utilisant la librairie pywin32, capable d'envoyer des touches.

 - La classe `KeyPresser` met le focus sur l'application "Firefox". (C'est pour ça que le script ne marche qu'avec Firefox, en fait il suffirait de changer le nom de l'application dans la classe.

 - Démarrage d'une boucle infinie, qui va exécuter toutes les étapes listées ci-dessous.

 - Exécution de la fonction `fish_line_analyzer.analyze` :

	 - Fonction `_make_screenshot_main_line` : screenshot de la fish_line (zone de 1 pixel de hauteur).

	 - Fonction `_reset_screenshot_values` et `_process_screenshot` : Mise à jour des variables internes :

		 - `x_red_mark_1`, `x_red_mark_2` : positions de la marque rouge représentant la "zone critique" (zone dans laquelle doit se trouver le triangle, au moment où on appuie sur une touche, pour réussir un perfect catch). La marque rouge fait deux pixels de large, c'est pour ça qu'il y a deux variables. Elles peuvent être toutes les deux égales à None lorsque la marque rouge n'est pas présente. De plus, la marque rouge est parfois présente, mais non détectée : lorsque le triangle est proche de la marque rouge, les couleurs se mélangent.

         - `x_triangle` : position de la pointe du triangle sur la fish_line.Peut être None lorsqu'aucun triangle n'est présent. À priori, lorsqu'il est présent, on parvient toujours à le détecter, grâce à des approximations sur les couleurs.

         - `cyan_dominant` : True : plus de 50% des pixels de la fish_line sont de la couleur turquoise spécifique. Cette vérification permet de s'assurer que la zone de pêche n'est pas actuellement en surbrillance verte ou rouge.

     - Fonction `_refresh_current_state` :

         - Mise à jour éventuelle de la variable `x_red_mark_consistent`. Correspond à la position de la zone critique de perfect catch (x_red_mark_1), même lorsque x_red_mark_1 est devenu None à cause du triangle qui passait devant. `x_red_mark_consistent` n'est remis à None que lorsqu'un catch a été effectué (perfect ou pas), c'est à dire lorsque la zone de pêche se met en surbrillance verte ou rouge.

         - Le jeu de Fishing possède une difficulté supplémentaire : lorsqu'on atteint un niveau de streak assez haut, la marque rouge n'est plus présente à l'écran. Dans ce cas, `x_red_mark_1` et `x_red_mark_consistent` restent None. On exécute alors la fonction `analyze` de la classe `FishSubLineAnalyzer` :

            - Capture d'écran de la "sub_fish_line" (ligne de pixel de même largeur que la fish_line, mais située 5 pixels en dessous).

            - Analyse de cette ligne pour trouver les deux pixels les plus turquoise possibles. Mise à jour des variables internes `x_critical_zone_1` et `x_critical_zone_2`. `FisfLineAnalyzer.x_red_mark_consistent` prendra la valeur de `x_critical_zone_1`.

            - Cette fonction d'analyse de la sub_line n'est effectuée que si un triangle a été repéré. Tant qu'il n'y a pas de triangle, la zone critique de perfect catch est peut-être en train de se déplacer (pour passer de l'ancienne position à la nouvelle position). Donc on attend d'être sûr que le déplacement soit fini.

         - La classe `FishSubLineAnalyzer` redétermine systématiquement la variable `fst_cur`. Cette variable sera récupérée par le code extérieur. Elle renseigne l'état actuel de la fish_line. Les différentes valeurs possibles d'état sont décrites au début du fichier `fish_line_analyzer.py`. Voir l'enum `FISHING_STATE`.

 - Après avoir appelé `fish_line_analyzer.analyze`, le code de la boucle infinie récupère la variable `fish_line_analyzer.fst_cur`

 - Si `fst_cur` a la valeur spécifique `fst.SEND_SIGNAL`, la classe `KeyPresser` envoie un appui de touche à l'application Firefox. Le jeu accepte n'importe quelle touche. Donc arbitrairement, on simule un appui sur "a".

 - Si `fst_cur` a changé de valeur par rapport à l'itération de boucle précédente : log de l'ancienne et de la nouvelle valeur dans la console.

 - Pour ne pas trop pourrir les performances, on attend un certain nombre de millisecondes entre deux itérations de boucle. Ce "certain nombre" dépend de fst_cur. Par exemple, lorsque la fish_line est en surbrillance, on n'est pas obligé de contrôler très fréquemment ce qu'il se passe à l'écran, car un nouveau triangle n'apparaîtra pas immédiatement. Tandis que lorsque le triangle est proche de la zone critique, il faut contrôler beaucoup plus fréquemment. Les correspondances "état -> temps d'attente" sont définis dans le dictionnaire `main.DICT_DELAY_FROM_FISHING_STATE`.

 - Retour au début de la boucle inifini, et ainsi de suite, jusqu'à l'infini, donc.

# Trucs qui pourraient être améliorés #

WIP

