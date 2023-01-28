import nltk
from nltk.tokenize import word_tokenize
from nltk.chunk import ne_chunk

# Charger le fichier wsj_0010_sample.txt
with open("../../data/wsj_0010_sample.txt", "r") as f:
    text = f.read()

# Tokeniser le texte en mots
words = word_tokenize(text)

# Tagger les mots avec des marqueurs de partie de discours
tagged_words = nltk.pos_tag(words)

# Extraire les entités nommées
named_entities = ne_chunk(tagged_words)

# Écrire les entités nommées dans un fichier
with open("../../data/wsj_0010_sample.txt.ne.nltk", "w") as f:
    for chunk in named_entities:
        if hasattr(chunk, 'label'):
            f.write(chunk.label() + ": " + " ".join([i[0] for i in chunk]) + "\n")
