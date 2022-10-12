import os
from nltk.tag import StanfordNERTagger
import pandas as pd
#Set environmental variables programmatically.
#Set the classpath to the path where the jar file is located
os.environ['CLASSPATH'] = "<path to the file>/stanford-ner-2015-04-20/stanford-ner.jar"

#Set the Stanford models to the path where the models are stored
os.environ['STANFORD_MODELS'] = '<path to the file>/stanford-corenlp-caseless-2015-04-20-models/edu/stanford/nlp/models/ner'

#Set the java jdk path
java_path = "C:/Program Files/Java/jdk1.8.0_161/bin/java.exe"
os.environ['JAVAHOME'] = java_path


#Set the path to the model that you would like to use
stanford_classifier  =  '<path to the file>/stanford-corenlp-caseless-2015-04-20-models/edu/stanford/nlp/models/ner/english.all.3class.caseless.distsim.crf.ser.gz'

#Build NER tagger object
st = StanfordNERTagger(stanford_classifier)

#A sample text for NER tagging
text = 'srinivas ramanujan went to the united kingdom. There he studied at cambridge university.'

#Tag the sentence and print output
tagged = st.tag(str(text).split())
print(tagged)
