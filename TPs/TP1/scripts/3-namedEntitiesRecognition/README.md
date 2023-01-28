# **Extraction d'entités nommées avec NLTK**

Le code importe les bibliothèques NLTK (Natural Language Toolkit) et utilise les fonctions word_tokenize pour diviser le texte en mots, pos_tag pour tagger chaque mot avec un marqueur de partie de discours et ne_chunk pour extraire les entités nommées.

Il ouvre ensuite un fichier texte nommé "wsj_0010_sample.txt" et le lit, puis utilise les fonctions précédemment importées pour tokeniser les mots, les tagger avec des marqueurs de partie de discours et extraire les entités nommées.

Les entités nommées sont ensuite écrites dans un fichier nommé "wsj_0010_sample.txt.ne.nltk".

Il y a un deuxième code qui est similaire mais il ajoute une étape de remplacement des labels de l'entité nommée en utilisant un dictionnaire my_dict. Il écrit le résultat dans un fichier nommé "wsj_0010_sample2.txt.ne.nltk"