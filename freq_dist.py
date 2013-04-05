import nltk
from nltk.classify import NaiveBayesClassifier

def word_feats(words):
    return dict([(word, True) for word in words])

f = open("tout.txt","r")
lines = f.readlines()
f.close()

typedict = {1:"addition" , 2:"reverse" , 3 :"telescopic" , 4:"homophones", 5:"embedded construction" , 6: "multiple definition" , 7:"cryptic definition" , 8:"anagram" , 9:"noncryptic easy" , 10:"general knowledge"}

count = []
for i in xrange(0,10):
  count.append(0)
string1 = []
string2 = []
string3 = []
string4 = []
string5 = []
string6 = []
string7 = []
string8 = []
string9 = []
i = 0
while(i<(len(lines)-3)):
	try:
		num_categ = int(lines[i+1][1])
	except:
		print i
	categ = typedict[num_categ]
	x = (word_feats(lines[i].split()),categ)
	if (num_categ == 1):
		count[0] +=1
		for x in lines[i].split():
			string1.append(x)
	if (num_categ == 2):
		count[1] +=1
		for x in lines[i].split():
			string2.append(x)
	if (num_categ == 3):
		count[2] +=1
		for x in lines[i].split():
			string3.append(x)
	if (num_categ == 4):
		count[3] +=1
		for x in lines[i].split():
			string4.append(x)
	if (num_categ == 5):
		count[4] +=1
		for x in lines[i].split():
			string5.append(x)
	if (num_categ == 6):
		count[5] +=1
		for x in lines[i].split():
			string6.append(x)
	if (num_categ == 7):
		count[6] +=1
		for x in lines[i].split():
			string7.append(x)
	if (num_categ == 8):
		count[7] +=1
		for x in lines[i].split():
			string8.append(x)
	if (num_categ == 9):
		count[8] +=1
		for x in lines[i].split():
			string9.append(x)
	i = i + 2

all_words = nltk.FreqDist(w.lower() for w in string1)
all_words1 = nltk.FreqDist(w.lower() for w in string2)
all_words2 = nltk.FreqDist(w.lower() for w in string3)
all_words3 = nltk.FreqDist(w.lower() for w in string4)
all_words4 = nltk.FreqDist(w.lower() for w in string5)
all_words5 = nltk.FreqDist(w.lower() for w in string6)
all_words6 = nltk.FreqDist(w.lower() for w in string7)
all_words7 = nltk.FreqDist(w.lower() for w in string8)
all_words8 = nltk.FreqDist(w.lower() for w in string9)
print all_words7
print count
