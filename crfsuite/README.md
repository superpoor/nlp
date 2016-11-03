# Commands
- To generate train.txt data: ```python gen_train.txt```
- To generate crfsuite train data from train.txt: ```cat train.txt | ./ner.py > train.crfsuite.txt```
- To generate crfsuite test data from test.txt: ```cat test.txt | ./ner.py > test.crfsuite.txt```
- To train and test at same time, print result, accuracy: ```crfsuite learn -e2 train.crfsuite.txt test.crfsuite.txt```
- To train from crfsuite train data to model: ```crfsuite learn -m API.model train.crfsuite.txt```
- To run model with crfsuite test data and visual result: ```crfsuite tag -r -m API.model test.crfsuite.txt```
