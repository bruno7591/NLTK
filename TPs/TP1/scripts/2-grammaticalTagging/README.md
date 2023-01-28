# **Extraction de mots composés avec NLTK**

Ce code utilise la bibliothèque NLTK (Natural Language Toolkit) pour extraire les mots composés d'un fichier de texte. Il commence par charger un fichier nommé **_"wsj_0010_sample.txt"_** en utilisant la méthode **_open()_** en mode lecture ("r"). Le contenu du fichier est ensuite stocké dans une variable text.

Ensuite, le code utilise la fonction word_tokenize de NLTK pour décomposer le texte en mots et stocker ces mots dans la variable words. Il utilise également la fonction **_pos_tag_** de NLTK pour assigner des marqueurs de partie de discours aux mots dans la variable **_tagged_words_**.

Le code crée ensuite une grammaire pour extraire les mots composés en utilisant la fonction RegexpParser de NLTK. La grammaire est définie comme une expression régulière qui décrit les mots composés comme étant soit un adjectif suivi d'un nom **_(<JJ><NN>)_**, deux noms consécutifs **_(<NN><NN>)_**, un adjectif suivi de deux noms consécutifs **_(<JJ><NN><NN>)_** ou deux adjectifs suivi d'un nom **_(<JJ><JJ><NN>)_** . Cette grammaire est ensuite utilisée pour parser les mots étiquetés dans la variable chunk_parser.

Enfin, le code écrit les mots composés extraits dans un nouveau fichier nommé **_"wsj_0010_sample2.txt.chk.nltk"_** en utilisant la méthode **_open()_** en mode écriture ("w").