import nltk

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
                        if lineNltk[1] == lineRef[1] :
                            validate += 1
                        univNltk.write(f"{lineNltk[0]}\t{lineNltk[1]}\n")
                        univRef.write(f"{lineRef[0]}\t{lineRef[1]}\n")
                        print("Comparing labels : " + lineNltk[1] + " (Nltk) & " + lineRef[1] + " (Ref)")
                        print("          for the word : " + lineNltk[0])
                        print("          accuracy : " + str(round((validate/compteur)*100,5)) + "%")
                        print()