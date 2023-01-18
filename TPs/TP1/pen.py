# Importation des modules nécessaires
import re

# Chargement de la table de correspondance
correspondance = {}
with open("POSTags_PTB_Universal.txt") as f:
    for ligne in f:
        ptb, univ = ligne.strip().split()
        correspondance[ptb] = univ

# Ouverture et lecture des fichiers d'entrée
with open("wsj_0010_sample.txt.pos.nltk") as f_nltk, open("wsj_0010_sample.pos.ref") as f_ref:
    # Lecture du contenu des fichiers
    contenu_nltk = f_nltk.read()
    contenu_ref = f_ref.read()


correspondance.pop('(', None)
correspondance.pop(')', None)

# Remplacement des étiquettes Penn TreeBank par les étiquettes universelles dans le contenu des fichiers
for ptb, univ in correspondance.items():   
   contenu_nltk = re.sub(ptb, univ, contenu_nltk)
   contenu_ref = re.sub(ptb, univ, contenu_ref)
correspondance['('] = '.'
correspondance[')'] = '.'
# Écriture du contenu modifié dans les fichiers de sortie
with open("wsj_0010_sample.txt.pos.nltk.univ", "w") as f_nltk, open("wsj_0010_sample.txt.pos.ref.univ", "w") as f_ref:
    f_nltk.write(contenu_nltk)
    f_ref.write(contenu_ref)
