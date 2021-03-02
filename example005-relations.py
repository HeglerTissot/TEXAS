import json
import texas as tx

# create a document
mydoc1 = tx.Document("Hello world!!! How are you today?", "en")
mydoc1.meta().set("authors","hegler,yiwen,celine,yuqian")
mydoc1.date().setTimestamp("2021-01-19T14:44") # ??
mydoc1.setTokenList( ["Hello", "world", "!","!","!","How","are","you","today","?"] )
mydoc1.addTokenView( "POS", ["?", "NOUN", "PUNCT","PUNCT","PUNCT","?","VERB","PRON","?","PUNCT"] )
mydoc1.setSentenceList( [5,10] )

# mydoc1.addSpanView( "NER0", [ {"label":"SOMETHING", "start_token":1, "final_token":2} ] )
mydoc1.addSpanView( "NER0", pType = "custom" )
mydoc1.addSpanAnns( "NER0", [ {"label":"SOMETHING", "start_token":1, "final_token":2} , {"label":"QUESTION", "start_token":9, "final_token":10} ] )
mydoc1.addSpanAnns( "NER0", {"label":"WORLD", "token_index":7} )

mydoc1.addRelationView( "RELATION0" , pType = "ignore") # , ["?", "NOUN", "PUNCT","PUNCT","PUNCT","?","VERB","PRON","?","PUNCT"] )
mydoc1.addRelationRoot( pViewName = "RELATION0" , pRelationName = "R0", pRootType = "predicate", pRootSpan = {"label":"be", "token_index":6} ) 

# create another document reversing from the previous document JSON 
mydoc2 = tx.reverse(mydoc1.TAS())

print("==========")
print("mydoc2")
print("----------")
print( "--- Token List" )
print( mydoc2.getTokenList() )
print( "--- Token Info" )
print( json.dumps( mydoc2.getTokenInfo() ) )
print( "--- Sentence Info" )
print( json.dumps( mydoc2.getSentenceInfo() ) )
print( "--- Document TAS" )
print( json.dumps(mydoc2.TAS()) )


print("")
print("end!")
print("")

