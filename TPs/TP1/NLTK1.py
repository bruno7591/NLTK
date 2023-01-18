import nltk
with open('wsj_0010_sample.txt', 'r') as f:
    text = f.read()
tokens = nltk.word_tokenize(text)
tagged_tokens = nltk.pos_tag(tokens)
with open('wsj_0010_sample.txt.pos.nltk', 'w') as f:
    for token in tagged_tokens:
        f.write(token[0] + '\t' + token[1] + '\n')
