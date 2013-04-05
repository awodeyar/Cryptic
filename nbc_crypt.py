import nltk.classify.util
from nltk.classify import NaiveBayesClassifier

def word_feats(words):
    return dict([(word, True) for word in words])

f = open("tout.txt","r")
lines = f.readlines()
f.close()

typedict = {1:"addition" , 2:"reverse" , 3 :"telescopic" , 4:"homophones", 5:"embedded construction" , 6: "multiple definition" , 7:"cryptic definition" , 8:"anagram" , 9:"noncryptic easy" , 10:"general knowledge"}

clues_train = []
i = 0
while(i<(len(lines)-1)):
  num_categ = lines[i+1]
	categ = typedict[num_categ]
	x = (word_feats(lines[i].split()),categ)
	clues_train.append(x)import nltk.classify.util
from nltk.classify import NaiveBayesClassifier

def word_feats(words):
    return dict([(word, True) for word in words])

f = open("tout.txt","r")
lines = f.readlines()
f.close()

typedict = {1:"addition" , 2:"reverse" , 3 :"telescopic" , 4:"homophones", 5:"embedded construction" , 6: "multiple definition" , 7:"cryptic definition" , 8:"anagram" , 9:"noncryptic easy" , 10:"general knowledge"}

clues_train = []
i = 0
while(i<(len(lines)-1)):
  num_categ = lines[i+1]
	categ = typedict[num_categ]
	x = (word_feats(lines[i].split()),categ)
	clues_train.append(x)
