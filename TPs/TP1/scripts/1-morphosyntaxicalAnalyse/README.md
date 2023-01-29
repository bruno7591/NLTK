# **POS Tagging avec NLTK**

## **Partie 1 - Génération de tags**

Ce script permet de lire le fichier et d'ajouter les tags correspondants à chaque mots dans le texte. Pour s'assurer que la mesure de la précision soit cohérente, on s'assure que les listes des mots dans le fichier obtenu et dans le fichier de référence soit les mêmes. On vérifie donc avant l'ajout d'un mot dans le fichier obtenu, que ce mot match avec le mot dans le fichier référence.

## **Partie 2 - Comparaison des tags et utilisation des tags universels**

Ce script permet quant à lui de faire correspondre les tags PTB avec les tags utilisés par défaut par NLTK. Pour ce faire, on parcours la table de correspondance entre les tags universels et PTB qu'on ajoute dans un dictionnaire sous forme de paire clé-valeur. Une fois cela fait, on parcours le fichier obtenu et on change les tags pour mettre les tags universels. Entre temps, on calcule la précision avec les tags universels.