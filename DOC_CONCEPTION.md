# Document de conception de Anti-Idle-Fish-Streaker #

## Trucs réutilisables pour d'autres scripts ##

 - `my_logging.py` : config à l'arrache de la librairie logging. En tout cas, ça écrit des accents sur la sortie standard sans se faire chier avec l'encodage.

 - `colrtool.py` : conversion de couleurs RGB -> HSV.

 - `screen_shotter.py` : capture de l'écran (tout, ou une zone spécifique), enregistrement en bmp, récupération des pixels. Il manque juste un peu de doc.

 - `fish_line_detector.find_first_color` : fonction parcourant une ligne ou une colonne d'une capture d'écran, pour trouver un pixel correspondant / ne correspondant pas à une couleur spécifique.

## Déroulement global des actions ##

 - Fonction `fish_line_detector.detect` :

 	- Parcours de la colonne de pixel x=900. Détection du premier pixel turquoise corresondant exactement à la couleur de la zone de pêche.

	- Si rien trouvé, on quitte la fonction. Et le script se termine avec l'exception "impossible de trouver la ligne de fishing à l'écran".

 	- Sinon, parcours horizontal de la ligne comportant le pixel turquoise. afin de déterminer où commence et où finit la "fish_line". Il s'agit de la ligne en haut du trapèze, sur laquelle se trouve la pointe supérieur du triangle qui passe.

 - les variables `y_line, x1_line, x2_line` permettent de repérer la fish\_line sur l'écran.

 - Instanciation d'une classe `FishLineAnalyzer` (effectue des copies d'écran de la fish\_line et les analyse), et d'une classe `FishSubLineAnalyzer` (effectue des copies d'écran d'une ligne située 5 pixels en dessous de la fish\_line).

 - L'instance de `FishSubLineAnalyzer` est transmise à `FishLineAnalyzer`.

 - Instanciation d'une classe `KeyPresser` : classe utilisant la librairie pywin32, capable d'envoyer des appuis de touches.

 - La classe `KeyPresser` met le focus sur l'application "Firefox". (C'est pour ça que le script ne marche qu'avec Firefox, il suffirait de changer le nom de l'application dans `KeyPresser`).

 - Démarrage d'une boucle infinie, qui va exécuter toutes les étapes listées ci-dessous.

 - Exécution de la fonction `fish_line_analyzer.analyze` :

	 - Exécution de la fonction `_make_screenshot_main_line` : screenshot de la fish\_line (une zone de 1 pixel de hauteur).

	 - Exécution des fonctions `_reset_screenshot_values` et `_process_screenshot`, pour mettre à jour les variables internes suivantes :

		 - `x_red_mark_1`, `x_red_mark_2` : positions de la marque rouge représentant la "zone critique" (zone dans laquelle doit se trouver le triangle, au moment où on appuie sur une touche, pour réussir un perfect catch). La marque rouge fait deux pixels de large, c'est pour ça qu'il y a deux variables. Elles peuvent être None lorsque la marque rouge est non présente, ou non détectée. La non-détection peut survenir lorsque le triangle est proche de la marque, dans ce cas les couleurs des pixels se mélangent.

         - `x_triangle` : position de la pointe du triangle sur la fish\_line. Peut être None lorsqu'aucun triangle n'est présent. À priori, on parvient toujours à le détecter, grâce à des approximations sur les couleurs.

         - `cyan_dominant` : Booléen. Vaut True lorsque plus de 50% des pixels de la fish\_line sont de la couleur turquoise spécifique. Cette vérification permet de s'assurer que la zone de pêche n'est pas actuellement en surbrillance verte ou rouge.

     - Exécution de la fonction `_refresh_current_state` :

         - Mise à jour éventuelle de la variable `x_red_mark_consistent`. Correspond à la position de la zone critique de perfect catch, c'est à dire `x_red_mark_1`. Mais on garde la valeur lorsque `x_red_mark_1` redevient None à cause du triangle qui passe devant. `x_red_mark_consistent` n'est remis à None que lorsqu'un catch a été effectué, c'est à dire lorsque la zone de pêche se met en surbrillance verte ou rouge.

         - Le jeu de Fishing possède une difficulté supplémentaire : lorsqu'on atteint un niveau de streak assez haut, la marque rouge n'est plus présente à l'écran. Dans ce cas, `x_red_mark_1` et `x_red_mark_consistent` restent None. On exécute alors la fonction `analyze` de la classe `FishSubLineAnalyzer`. Elle effectue les actions suivantes :

            - Capture d'écran de la "sub\_fish\_line" (ligne de pixel de même largeur que la fish\_line, mais située 5 pixels en dessous).

            - Analyse de cette ligne pour trouver les deux pixels les plus turquoise possibles. Mise à jour des variables internes `x_critical_zone_1` et `x_critical_zone_2`. `FishLineAnalyzer.x_red_mark_consistent` prendra la valeur de `x_critical_zone_1`.

            - Cette fonction d'analyse de la sub_line n'est effectuée que si un triangle a été repéré. Car tant qu'il n'y a pas de triangle, la zone critique de perfect catch est peut-être en train de se déplacer, pour passer de l'ancienne position à la nouvelle position.

         - Redétermination systématique de la variable `FishLineAnalyzer.fst_cur`. Elle renseigne l'état actuel de la fish\_line. Les différentes valeurs possibles sont décrites par l'enum `FISHING_STATE`, dans le  fichier `fish_line_analyzer.py`.

 - Après avoir exécuté `fish_line_analyzer.analyze`, la boucle infinie récupère la variable `fst_cur`.

 - Si `fst_cur` a la valeur spécifique `fst.SEND_SIGNAL`, la classe `KeyPresser` envoie un appui de touche à l'application Firefox. Le jeu accepte n'importe quelle touche. Donc arbitrairement, on simule un appui sur "a".

 - Si `fst_cur` a changé de valeur par rapport à l'itération de boucle précédente : log de l'ancienne et de la nouvelle valeur dans la console.

 - Pour ne pas trop pourrir les performances, on attend un certain nombre de millisecondes entre deux itérations de boucle, selon la valeur de `fst_cur`. Par exemple, lorsque la fish\_line est en surbrillance, on n'est pas obligé de contrôler très fréquemment ce qu'il se passe à l'écran, car un nouveau triangle n'apparaîtra pas immédiatement. Tandis que lorsque le triangle est proche de la zone critique, il faut contrôler beaucoup plus fréquemment. Les correspondances "état -> temps d'attente" sont définis dans le dictionnaire `main.DICT_DELAY_FROM_FISHING_STATE`.

 - Retour au début de la boucle inifini, et ainsi de suite, jusqu'à l'infini, donc.

# Trucs qui pourraient être améliorés #

 - Détecter quel navigateur internet est en cours d'exécution, et se focuser sur le premier trouvé, au lieu de prendre que Firefox.

 - Si le focus n'est plus sur le navigateur, arrêter d'envoyer des appuis de touche, voire carrément arrêter le script. Ça évitera des bêtises.

 - L'analyse des copies d'écran ne marche pas tout le temps, et les appuis de touche ne sont pas toujours envoyés au bon moment. Je ne sais pas trop pourquoi. Il faudrait peut-être revoir complètement le principe de fonctionnement. Au lieu d'attendre que le triangle soit dans la zone critique, on pourrait estimer sa vitesse et la distance restante à parcourir, ce qui permettrait de savoir, à l'avance, quand envoyer l'appui de touche.

 - Les TODO dans le code.

