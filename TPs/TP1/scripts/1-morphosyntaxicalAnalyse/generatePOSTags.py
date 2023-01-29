import nltk

# Open the file 'wsj_0010_sample.txt' and read the content
with open('../../data/wsj_0010_sample.txt', 'r') as f:
    text = f.read()

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Tag each token with its grammatical type
tagged_tokens = nltk.pos_tag(tokens)

# Open the reference file 'wsj_0010_sample.pos.ref' and read its content
with open('../../data/wsj_0010_sample.pos.ref', 'r') as f:
    tmpText = f.read().split()

# Store the reference words in a list 'refText'
refText = []
for i in range(len(tmpText)) :
    # We only keep the word, not the tag, this will be usefull for writing in the target file
    if i % 2 == 0 :
        refText.append(tmpText[i])

# Write the tokenized words with their grammatical type in a new file
indice = 0
with open('../../data/wsj_0010_sample.txt.pos.nltk', 'w') as f:
    for token in range(len(refText)):
        # Check if the token is equal to the reference word, if not, we have to skip the word to match the ordre of the ref file 
        if (tagged_tokens[token][0] == refText[indice]):
            # Write the token and its grammatical type
            f.write(tagged_tokens[token][0] + '\t' + tagged_tokens[token][1])
            # Add a new line if it is not the last word
            if token < len(refText) :
                f.write("\n")
        else :
            # Increment the token index
            token += 1
            # Write the token and its grammatical type
            f.write(tagged_tokens[token][0] + '\t' + tagged_tokens[token][1])
            # Add a new line if it is not the last word
            if token < len(refText) :
                f.write("\n")
        # Increment the reference word index
        indice += 1
