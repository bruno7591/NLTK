import nltk
from nltk.tokenize import word_tokenize
from nltk.chunk import ne_chunk

# Charger le fichier wsj_0010_sample.txt
with open("../data/wsj_0010_sample.txt", "r") as f:
    text = f.read()

# Tokeniser le texte en mots
words = word_tokenize(text)

# Tagger les mots avec des marqueurs de partie de discours
tagged_words = nltk.pos_tag(words)

# Extraire les entités nommées
named_entities = ne_chunk(tagged_words)

my_dict = {"ORGANIZATION": "ORG", 
           "PERSON": "PERS", 
           "LOCATION": "LOC", 
           "DATE": "MISC", 
           "TIME": "MISC", 
           "MONEY": "MISC", 
           "PERCENT": "MISC", 
           "FACILITY": "ORG", 
           "GPE": "LOC"}

# Écrire les entités nommées dans un fichier
with open("../data/wsj_0010_sample2.txt.ne.nltk", "w") as f:
    for chunk in named_entities:
        if hasattr(chunk, 'label'):
            f.write(my_dict[chunk.label()] + ": " + " ".join([i[0] for i in chunk]) + "\n")