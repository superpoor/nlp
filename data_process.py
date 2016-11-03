import json
import re
import xml.sax
import sys
from HTMLParser import HTMLParser
import nltk

MAX_THREADS = 100
MAX_POSTS = 500

cnt_threads = 0
cnt_posts = 0

posts = []
cnt_answer_in_posts = {}

def removeHtmlTag(s):
  newS = re.sub('(<.*?>)|(</.*?>)', '', s) \
    .replace("\n", " ", 1000000000) \
    .replace("\r", " ", 1000000000)
  return HTMLParser().unescape(newS) \
    .replace(u'\xa0', ' ', 100000000)


class TerminateError(xml.sax.SAXException):
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return repr(self.value)

class MyHandler( xml.sax.ContentHandler ):
  def startElement(self, name, attrs):
    global cnt_posts, cnt_threads

    if not name == "row":
      return
    if cnt_threads >= MAX_THREADS and cnt_posts >= MAX_POSTS:
      raise TerminateError("Reach enough threads and posts")

    posts.append(removeHtmlTag(attrs["Body"]))

    cnt_posts += 1
    if attrs["PostTypeId"] == "1":
      cnt_threads += 1
    else:
      cnt_answer_in_posts[attrs["ParentId"]] = cnt_answer_in_posts.get(attrs["ParentId"], 0) + 1

parser = xml.sax.make_parser()
parser.setContentHandler(MyHandler())

try:
  try: 
    sourcefile = sys.argv[1]
  except IndexError as e:
    sourcefile = "Posts.xml"
  print("Reading from " + sourcefile)
  parser.parse(sourcefile)
except TerminateError as e:
  print e.__str__()

with open('data2.json', 'w') as out_file:
  json.dump(posts, out_file, indent=4, encoding="utf8")

cnt_words = 0
for post in posts:
  cnt_words += len(post.split(" "))

print "Number of questions = " + cnt_threads.__str__()
print "Number of answers = " + (cnt_posts - cnt_threads).__str__()
print "Average words in each post = " + (cnt_words / cnt_posts).__str__()

cnt_answers = [0, 0, 0, 0, 0]

for key in cnt_answer_in_posts:
  x = min(4, cnt_answer_in_posts[key])
  cnt_answers[x] += 1

for i in range(1, 4):
  print "There are %d questions having %d answers" % (cnt_answers[i], i)
print "There are %d questions having more then 3 answers" % (cnt_answers[4])

