from nltk.stem.snowball import EnglishStemmer
import nltk
import json
import re

posts = json.load(open("data2.json"))
stop_word = ['a', 'the', 'of', 'and']
stemmer = EnglishStemmer()
word_cnt = 0
stem_dict = {}


def compute(s):
  global word_cnt
  tokens = nltk.word_tokenize(s)
  for token in tokens:
    stem =  stemmer.stem(token)
    stem = stem.encode('utf8')
    if re.match('\w+$', stem):
      word_cnt += 1
      if not stem_dict.has_key(stem):
        stem_dict[stem] = []
      stem_dict[stem].append(token.encode('utf8'))

# compute stem_dict
for post in posts:
  compute(post["content"])
  for answer in post["answer"]:
    compute(answer)

# compute stem_cnt: list of stem with corresponding number of words of this stem
stem_cnt = []
for stem in stem_dict.keys():
  stem_cnt.append((len(stem_dict[stem]), stem))

# compute output
stem_cnt.sort(reverse=True)
most_fre_stem = []
stem_out = 0
str_out = ''
for stem in stem_cnt:
  if not stem[1] in stop_word:
    most_fre_stem.append(stem[1])
    str_out += 'Stem \'' + stem[1] + '\' used ' + stem[0].__str__() + ' times.\n'
    str_out += 'Original words: ' + list(set(stem_dict[stem[1]])).__str__() + '.\n'
    stem_out += 1
    if stem_out >= 20: break

print ('******************************\nTop 20-most frequent stems: ' + most_fre_stem.__str__())
print str_out






