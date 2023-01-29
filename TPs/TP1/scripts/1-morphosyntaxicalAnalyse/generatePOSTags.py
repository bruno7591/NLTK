import nltk

with open('../../data/wsj_0010_sample.txt', 'r') as f:
    text = f.read()

tokens = nltk.word_tokenize(text)
tagged_tokens = nltk.pos_tag(tokens)

with open('../../data/wsj_0010_sample.pos.ref', 'r') as f:
    tmpText = f.read().split()

refText = []

for i in range(len(tmpText)) :
    if i % 2 == 0 :
        refText.append(tmpText[i])

indice = 0
with open('../../data/wsj_0010_sample.txt.pos.nltk', 'w') as f:
    for token in range(len(refText)):
        if (tagged_tokens[token][0] == refText[indice]):
            f.write(tagged_tokens[token][0] + '\t' + tagged_tokens[token][1])
            if token < len(refText) :
                f.write("\n")
        else :
            token += 1
            f.write(tagged_tokens[token][0] + '\t' + tagged_tokens[token][1])
            if token < len(refText) :
                f.write("\n")
        indice += 1
