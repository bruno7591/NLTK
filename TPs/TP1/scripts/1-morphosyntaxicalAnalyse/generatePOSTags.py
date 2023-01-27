import nltk

# Open the file 'wsj_0010_sample.txt' in read mode
with open('../../data/wsj_0010_sample.txt', 'r') as f:
    # Read the contents of the file and store it in the variable 'text'
    text = f.read()

# Tokenize the text into a list of words
tokens = nltk.word_tokenize(text)
# Apply parts of speech tags to each word in the list of tokens
tagged_tokens = nltk.pos_tag(tokens)

# Open a new file called 'wsj_0010_sample.txt.pos.nltk' in write mode
with open('../../data/wsj_0010_sample.txt.pos.nltk', 'w') as f:
    # Iterate through the list of tagged tokens
    for token in tagged_tokens:
        # Write each token and its POS tag to the new file
        f.write(token[0] + '\t' + token[1] + '\n')
        # Also print the token and its POS tag on screen, just for checking
        #print(token[0] + '\t' + token[1] + '\n')