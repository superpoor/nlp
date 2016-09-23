import nltk

sentences = [
  'This is a common question by those who have just rooted their phones',
  "I've unzipped zip files for custom kernels and noticed that the majority of the files that are being applied are in a /kernel folder. However that folder is unlisted when listing the root directories using both Root Explorer and ES File Explorer",
  'I understand that a factory reset is not enough in most cases',
  "I think you'd need to have a credit card that has a billing address in the US (or other supported country).",
  "I have a couple of accounts linked to my Google Photos app on my phone.",
  "One is my personal account and one is a shared company account.",
  "How can I stop applications and services from running?",
  "Please, please, please, please put down the task killer.",
  "There are some apps around that will claim to offer this functionality.",
  "I want to remove bloatware Velvet apk (Google app) from stock Android Marshmallow on a Nexus 5."
]

for s in sentences:
  print '*******************************************'
  print "Pos tagging sentences: \'" + s + "\'"
  tokens = nltk.word_tokenize(s)
  tagged = nltk.pos_tag(tokens)
  print tagged

