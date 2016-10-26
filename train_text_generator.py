import nltk
import json
import logging
import sys
from nltk.corpus import treebank
from nltk.chunk import *
from nltk.chunk.util import *
from nltk.chunk.regexp import *
from nltk import Tree

def main():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        # post_count = 0
        sentence_count = 0
        with open('test.txt', 'w') as output:
            for post in data:
                # if post_count > 50:
                if sentence_count > 5:
                    break
                # post_count += 1
                logging.info('*******************************************')
                logging.info("Pos tagging post: \'" + post + "\'")
                logging.info('*******************************************')
                sentences = post.split('. ')
                for s in sentences:
                    sentence_count += 1
                    tokens = nltk.word_tokenize(s)
                    tagged = nltk.pos_tag(tokens)
                    for tag in tagged:
                        logging.info(tag[0] + ' ' + tag[1])
                        # TODO: add rules to define structure of the sentence
                        try:
                            output.write(tag[0] + ' ' + tag[1] + '\n')
                        except UnicodeEncodeError as e:
                            logging.error(e)
                            continue
                    output.write('. . O' + '\n\n')
                    # entities = nltk.chunk.ne_chunk(tagged)
                    # output.write('\nStructure\n' + entities + '\n\n')
                    # output.write('chunking... \n' + unchunked_text + '\n\n')

root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

main()
