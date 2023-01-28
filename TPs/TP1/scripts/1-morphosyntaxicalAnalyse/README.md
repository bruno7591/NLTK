# **POS Tagging avec NLTK**

Ce code utilise la bibliothèque NLTK (Natural Language Toolkit) pour ajouter des étiquettes de parties du discours à un texte.

Il utilise le fichier **_'wsj_0010_sample.txt'_** en mode lecture, lit son contenu et le stocke dans la variable **_'text'_**. Ensuite, il tokenize le texte en une liste de mots avec **_'nltk.word_tokenize(text)'_** et applique des étiquettes de parties du discours à chaque mot dans la liste de tokens avec **_'nltk.pos_tag(tokens)'_**. Les résultats sont enregistrés dans un nouveau fichier **_'wsj_0010_sample.txt.pos.nltk'_** en mode écriture.

Ensuite, il crée un dictionnaire vide pour mapper les étiquettes de parties du discours **_PTB (Penn Treebank)_** vers les étiquettes universelles. Il utilise un fichier externe **_"POSTags_PTB_Universal.txt"_** pour remplir ce dictionnaire.

Il ouvre ensuite les fichiers contenant les textes POS taggés par NLTK et par une référence, et les compare. Il écrit les résultats dans les fichiers **_'wsj_0010_sample.txt.pos.univ.nltk'_** et **_'wsj_0010_sample.pos.univ.ref'_** en utilisant le dictionnaire de correspondance précédemment créé. Il calcule également la précision de l'analyseur NLTK par rapport à la référence et l'affiche à l'écran.