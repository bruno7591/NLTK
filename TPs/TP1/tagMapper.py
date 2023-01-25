
correspondance = {}
with open("POSTags_PTB_Universal.txt") as f:
    for ligne in f:
        ptb, univ = ligne.strip().split()
        correspondance[ptb] = univ

with open('wsj_0010_sample.txt.pos.nltk','r') as nltkText :
    with open('wsj_0010_sample.pos.ref','r') as refText :
        with open('wsj_0010_sample.txt.pos.univ.nltk','w') as univNltk :
            with open('wsj_0010_sample.pos.univ.ref','w') as univRef :
                nltktext = nltkText.readlines()
                reftext = refText.readlines()
                validate = 0
                compteur = 0
                for index in range(len(nltktext)) :
                    lineNltk = nltktext[index].split()
                    lineRef = reftext[index].split()
                    if lineNltk[0] == lineRef[0] :
                        compteur += 1
                        univRef.write(f"{lineRef[0]}\t{correspondance[lineRef[1]]}\n")
                        univNltk.write(f"{lineNltk[0]}\t{correspondance[lineNltk[1]]}\n")
                        if correspondance[lineRef[1]] == correspondance[lineNltk[1]] :
                            validate += 1

print("Accuracy : " + str(round((validate/compteur)*100,5)) + "%")
