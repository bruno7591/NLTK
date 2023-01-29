# Dictionary to map PTB POS tags to Universal POS tags
correspondance = {}

# Open the PTB-Universal POS tag mapping file
with open("../../data/POSTags_PTB_Universal.txt") as f:
    # For each line in the file
    for line in f:
        # Split the line by tab and store the PTB and Universal tags in separate variables
        ptb, univ = line.strip().split()
        # Map the PTB tag to the Universal tag in the dictionary
        correspondance[ptb] = univ

# Open the nltk tagged POS file and reference POS file
with open('../../data/wsj_0010_sample.txt.pos.nltk','r') as nltkText, open('../../data/wsj_0010_sample.pos.ref','r') as refText:
    # Open the files to write the Universal tagged POS data
    with open('../../data/wsj_0010_sample.txt.pos.univ.nltk','w') as univNltk, open('../../data/wsj_0010_sample.pos.univ.ref','w') as univRef:

        # Read the lines from the nltk tagged POS file and reference POS file
        nltktext = nltkText.readlines()
        reftext = refText.readlines()
        # Counter for the number of correct Universal POS tag matches
        validate = 0
        # Counter for the total number of words
        counter = 0
        # Loop through the nltk tagged POS data and reference POS data
        for index in range(len(nltktext)):
            # Split the line into word and tag
            lineNltk = nltktext[index].split()
            lineRef = reftext[index].split()
            # If the word in the nltk tagged POS data matches the reference POS data
            if lineNltk[0] == lineRef[0]:
                # Increment the counter for total words
                counter += 1
                # Write the reference word and Universal POS tag to the output file
                univRef.write(f"{lineRef[0]}\t{correspondance[lineRef[1]]}\n")
                # Write the nltk tagged word and Universal POS tag to the output file
                univNltk.write(f"{lineNltk[0]}\t{correspondance[lineNltk[1]]}\n")
                # If the Universal POS tags match, increment the counter for correct matches
                if correspondance[lineRef[1]] == correspondance[lineNltk[1]]:
                    validate += 1

# Print the accuracy of the Universal POS tagging
print("Accuracy : " + str(round((validate/counter)*100,5)) + "%")
