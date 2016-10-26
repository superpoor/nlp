# nlp

Questions:

In the execution trunk in data_process.py, what is "Posts.xml"?
- Posts.xml is not uploaded as it's a large file 

CRFSuite example usage: 
$ cat train.txt | python2 chunking.py > train.crfsuite.txt (train.txt was not included)
$ cat test.txt | python2 chunking.py > test.crfsuite.txt

$ crfsuite learn -m CoNLL2000.model train.crfsuite.txt
// create the model using the train data. Here we use test.crfsuite.txt instead of train.crfsuite.txt

$ crfsuite tag -r -m CoNLL2000.model test.crfsuite.txt
// test the testdata using the model. Run for result

$ crfsuite tag -qt -m CoNLL2000.model test.crfsuite.txt
// run for evaluation
