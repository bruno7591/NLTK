cd .\1-morphosyntaxicalAnalyse\
py .\generatePOSTags.py
cd ..
py .\evaluate.py ..\data\wsj_0010_sample.txt.pos.nltk ..\data\wsj_0010_sample.pos.ref
cd .\1-morphosyntaxicalAnalyse\
py .\matchingIdenticalUnivTags.py
cd ..
cd .\2-grammaticalTagging\
py .\extractingChunks.py
py .\extractingCompatibleChunks.py
cd ..
cd .\3-namedEntitiesRecognition\
py .\extractingNamedEntities.py
py .\convertingLabels.py