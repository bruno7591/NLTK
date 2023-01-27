# Create an empty dictionary to map PTB POS tags to Universal POS tags
correspondance = {}

# Open the file containing the PTB to Universal POS tag mapping
with open("../../data/POSTags_PTB_Universal.txt") as f:
    # Iterate through each line of the file
    for ligne in f:
        # Split each line by whitespace into two variables: PTB tag and Universal tag
        ptb, univ = ligne.strip().split()
        # Add the PTB tag as the key and the Universal tag as the value to the correspondance dictionary
        correspondance[ptb] = univ

# Open the files containing the POS tagged text from the NLTK tagger and the reference tagger
with open('../../data/wsj_0010_sample.txt.pos.nltk','r') as nltkText, open('../../data/wsj_0010_sample.pos.ref','r') as refText:
    # Open the files to write the mapped POS tags using the correspondance dictionary
    with open('../../data/wsj_0010_sample.txt.pos.univ.nltk','w') as univNltk, open('../../data/wsj_0010_sample.pos.univ.ref','w') as univRef:
        # Read the contents of the NLTK and reference POS tagged text files
        nltktext = nltkText.readlines()
        reftext = refText.readlines()
        # Initialize variables to store the number of correctly tagged words and the total number of words
        validate = 0
        compteur = 0
        # Iterate through the lines of both text files
        for index in range(len(nltktext)):
            # Split each line by whitespace to separate the word and POS tag
            lineNltk = nltktext[index].split()
            lineRef = reftext[index].split()
            # Check if the current word in both text files match
            if lineNltk[0] == lineRef[0]:
                # Increment the total word count
                compteur += 1
                # Write the current word and its mapped Universal POS tag from the correspondance dictionary to the univRef file
                univRef.write(f"{lineRef[0]}\t{correspondance[lineRef[1]]}\n")
                # Write the current word and its mapped Universal POS tag from the correspondance dictionary to the univNltk file
                univNltk.write(f"{lineNltk[0]}\t{correspondance[lineNltk[1]]}\n")
                # Check if the POS tag from the NLTK tagger matches the POS tag from the reference tagger
                if correspondance[lineRef[1]] == correspondance[lineNltk[1]]:
                    # Increment the count of correctly tagged words
                    validate += 1

# Print the accuracy of the NLTK POS tagger in comparison to the reference tagger
print("Accuracy : " + str(round((validate/compteur)*100,5)) + "%")
