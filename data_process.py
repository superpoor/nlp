import xml.etree.ElementTree as ET
from random import shuffle
import json

posts = {}

def parse(path):
  tree = ET.parse(path + "/Posts.xml")
  root = tree.getroot()

  for post in root:
    if post.attrib["PostTypeId"] == "1":
      id = int(post.attrib["Id"])
      posts[id] = {
        "id": id,
        "content": post.attrib["Body"],
        "answer": []
      }

  for post in root:
    if post.attrib["PostTypeId"] == "2":
      posts[int(post.attrib["ParentId"])]["answer"].append({
        "id": post.attrib["Id"],
        "content": post.attrib["Body"]
      })

parse('android.stackexchange.com')
posts2 = posts.values()
#shuffle(posts2)
out = posts2[0:200]

with open('data.json', 'w') as outfile:
  json.dump(out, outfile, indent=4)

num_answer = {}
words_cnt = 0

post_cnt = len(out)
for post in out:
  cnt = len(post["answer"])
  post_cnt += cnt
  num_answer[cnt] = num_answer.get(cnt, 0) + 1
  words_cnt += len(post["content"].split(" "))
  for answer in post["answer"]:
    words_cnt += len(answer["content"].split(" "))

print "Number of questions = " + len(out).__str__()
print "Number of answers = " + post_cnt.__str__()
cnt = 0
for i in range(4):
  cnt += num_answer.get(i, 0)
  print "There are " + num_answer.get(i, 0).__str__() + " questions have " + i.__str__() + " answers, " + (num_answer.get(i, 0) / 2.0).__str__() + "% percentage"

print "There are " + (200 - cnt).__str__() + " questions have more than 3 answers, " + ((200 - cnt)/ 2.0).__str__() + "% percentage"
print "Average of words in " + post_cnt.__str__() + " posts is " + (words_cnt / post_cnt).__str__()







