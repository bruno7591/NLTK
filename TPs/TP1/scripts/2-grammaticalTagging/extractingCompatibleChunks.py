import nltk
from nltk.tokenize import word_tokenize
from nltk.chunk import RegexpParser

# Charger le fichier wsj_0010_sample.txt
with open("../../data/wsj_0010_sample.txt", "r") as f:
    text = f.read()

# Tokeniser le texte en mots
words = word_tokenize(text)

# Tagger les mots avec des marqueurs de partie de discours
tagged_words = nltk.pos_tag(words)

# Créer une grammaire pour extraire les mots composés
chunk_grammar = "Compound: {(<JJ><NN>)|(<NN><NN>)|(<JJ><NN><NN>)|(<JJ><JJ><NN>)}"
#La condition est composée de :
#<DT>? : déterminant facultatif (0 ou 1)
#<JJ>* : une série d'adjectifs (0 ou plus)
#<NN> : un nom

chunk_parser = RegexpParser(chunk_grammar)
chunked_words = chunk_parser.parse(tagged_words)
print(type(chunked_words))

# Écrire les mots composés dans un fichier
with open("../../data/wsj_0010_sample2.txt.chk.nltk", "w") as f:
    for word in chunked_words:
        if isinstance(word, nltk.tree.Tree):
            if word.label() == "Compound":
                f.write(" ".join([i[0] for i in word.leaves()]) + "\n")