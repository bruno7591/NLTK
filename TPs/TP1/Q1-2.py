import nltk

with open('wsj_0010_sample.txt.pos.nltk','r') as nltkText :
    with open('wsj_0010_sample.pos.ref','r') as refText :
        reftext = refText.readlines()
        nltktext = nltkText.readlines()
        for i in range(len(reftext)):
            reftext[i] = reftext[i].split()
        for i in range(len(nltktext)):
            nltktext[i] = nltktext[i].split()
        for i in range(len(reftext)):
            try:
                if (reftext[i][0] != nltktext[i][0]):
                    #print(reftext[i], nltktext[i])
                    print(i)
            except Exception as e:
                print(reftext[i-1][0])
                pass