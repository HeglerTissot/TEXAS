import json
import texas as tx
import stanza

# ignore all the following "playing" segments

'''
nlp = stanza.Pipeline("pt")
text = "Eu não gosto daquela laranja que vejo no pomar."
doc = nlp(text)
for sentence in doc.sentences:
    print(sentence)
for token in doc.iter_tokens():
    print(token)

UDPipe
nlpD = spacy_udpipe.load("pt")
# nlpD = spacy_udpipe.load("pt").tokenizer
text = "
u não gosto daquela laranja que vejo no pomar.
"
doc = nlpD(text)

for t in doc:
    tok = t
    print(t, t.idx)
    
for sentence in doc.sents:
    sent = sentence
    print(sentence)


spacy
nlp = spacy.load("pt_core_news_sm")
text = "Eu não gosto daquela laranja que vejo no pomar."
doc = nlp(text)

>>> Italian !!!

nlp = spacy.load("it_core_news_sm")

text = "Apple vuole comprare una startup del Regno Unito per un miliardo di dollari."

doc = nlp(text)

for t in doc:
    tok = t
    print(t, t.idx, t.lemma_, t.pos_, t.tag_)



nlp = stanza.Pipeline("it")

text = "Apple vuole comprare una startup del Regno Unito per un miliardo di dollari."

doc = nlp(text)

for sentence in doc.sentences:
    print(sentence)
for token in doc.iter_tokens():
    print(token)

'''

# create a document

TXLang = "en"
TXText = "Sigmund Freud was an Austrian neurologist and the founder of psychoanalysis, a clinical method for treating psychopathology through dialogue between a patient and a psychoanalyst. Freud was born to Galician Jewish parents in the Moravian town of Freiberg, in the Austrian Empire."

TXSpacyModel = TXLang

nlp = stanza.Pipeline(TXSpacyModel)

doc = nlp(TXText)

index = -1
sentIndex = 0
nlpTokenList = []
nlpPOSList = []
nlpDEPList = []
nlpLemmaList = []
nlpSentenceEndPositions = []

for sentence in doc.sentences:
    sentIndex+=len(sentence.words)
    nlpSentenceEndPositions.append(sentIndex)
    for word in sentence.words:
        print(word.text, word.lemma, word.pos)
        index += 1
        nlpTokenList.append(word.text)
        nlpPOSList.append(word.pos)
        nlpLemmaList.append(word.lemma)
        
mydoc1 = tx.Document(TXText, TXLang)
# mydoc1.meta().set("generator","stanza")
# mydoc1.meta().set("model",TXSpacyModel)

'''
text = "Eu não gosto daquela laranja que de vejo no pomar."

Eu não gosto "de+aquela" laranja que vejo em+o pomar .
             "PREP+PRON"
             ["PREP","PRON"]

'''

mydoc1.setTokenList( nlpTokenList, indexed=True)
mydoc1.views().get("TOKENS").meta().set("generator","stanza")
mydoc1.views().get("TOKENS").meta().set("model",TXSpacyModel)
mydoc1.setSentenceList( nlpSentenceEndPositions )

mydoc1.addTokenView( "POS", nlpPOSList )
# no "DEP" annotations resulting from stanza
# mydoc1.addTokenView( "POS-DEP", nlpDEPList )
mydoc1.addTokenView( "LEMMA", nlpLemmaList )

# create another document reversing from the previous document JSON 
mydoc2 = tx.reverse(mydoc1.TAS())

print("==========")
print("mydoc2")
print("----------")
print( "--- Document TAS" )
print( json.dumps(mydoc2.TAS()) )
print( "--- Token List" )
print( mydoc2.getTokenList() )
print( "--- Token Info" )
print( json.dumps( mydoc2.getTokenInfo() ) )
print( "--- Sentence Info" )
print( json.dumps( mydoc2.getSentenceInfo() ) )

print("")
print("end!")
print("")

