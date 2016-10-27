import os
import nltk
from nltk.tag import SennaChunkTagger

#print os.environ['SENNA']

chktagger = SennaChunkTagger(os.environ['SENNA'])


sentences = [
  'Will String.trim() remove all spaces on these sides or just one space on each?',
  'If no such object exists, the map should be "wrapped" using the Collections.synchronizedMap method.'
]

with open('train.txt', 'w') as f:
  for s in sentences:
    tokens = nltk.word_tokenize(s)
    pos_tag = nltk.pos_tag(tokens)
    chunk_tag = chktagger.tag(tokens)
    #print chunk_tag

    for index, token in enumerate(tokens):
      f.write('O %s %s %s \n' % ( token, pos_tag[index][1], chunk_tag[index][1] ))

    f.write('\n')

  f.write('\n')

