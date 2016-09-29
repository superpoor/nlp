import json
import re
import xml.sax
from HTMLParser import HTMLParser

MAX_THREADS = 100
MAX_POSTS = 500

cnt_threads = 0
cnt_posts = 0

posts = []

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
    if cnt_threads >= 100 and cnt_posts >= 500:
      raise TerminateError("Reach enough threads and posts")

    posts.append({
      "type": attrs["PostTypeId"],
      "id": attrs["Id"],
      "content": removeHtmlTag(attrs["Body"]),
      "parentId": attrs.get("ParentId", -1)
    })

    cnt_posts += 1
    if attrs["PostTypeId"] == "1":
      cnt_threads += 1

parser = xml.sax.make_parser()
parser.setContentHandler(MyHandler())

try:
  parser.parse("Posts.xml")
except TerminateError as e:
  print e.__str__()

with open('data.json', 'w') as out_file:
  json.dump(posts, out_file, indent=4, encoding="utf8")

print "Number of threads = " + cnt_threads.__str__()
print "Number of posts = " + cnt_posts.__str__()






