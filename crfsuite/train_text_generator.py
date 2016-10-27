import os
import nltk
import json
import logging
import sys
from MyUtils import potential_API

from nltk.tag import SennaChunkTagger
chktagger = SennaChunkTagger(os.environ['SENNA'])

def main():
    logging.basicConfig(filename='sample.log', filemode='w', level=logging.DEBUG)
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        post_count = 0
        # sentence_count = 0
        total_count = len(data)
        break_point = total_count*3//4
        with open('train.txt', 'w') as train_f:
            with open('test.txt', 'w') as test_f:
                counting = 0
                API_count = 0
                API_set = set()
                for post in data:
                    # if post_count > 50:
                    # if sentence_count > 5:
                        # break
                    # post_count += 1
                    if counting > break_point:
                        f = test_f
                    else:
                        f = train_f
                    counting += 1

                    # logging.info('*******************************************')
                    # logging.info("Pos tagging post: \'" + post + "\'")
                    # logging.info('*******************************************')
                    sentences = nltk.tokenize.sent_tokenize(post)
                    for s in sentences:
                        tokens = nltk.word_tokenize(s)
                        pos_tag = nltk.pos_tag(tokens)
                        try:
                            chunk_tag = chktagger.tag(tokens)
                        except IndexError as e:
                            logging.error(e)
                            continue
                        #print chunk_tag

                        for index, token in enumerate(tokens):
                            try:
                                if '(' in token:
                                    if index > 0:
                                        if tokens[index-1] in potential_API:
                                            f.write('I-API %s %s %s \n' % ( token, pos_tag[index][1], chunk_tag[index][1] ))            
                                            continue
                                f.write('O %s %s %s \n' % ( token, pos_tag[index][1], chunk_tag[index][1] ))

                            except UnicodeEncodeError as e:
                                logging.error(e)
                                continue


                        f.write('\n')
                    logging.info(counting)
                    f.write('\n')

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
