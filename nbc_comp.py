import nltk
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier

def word_feats(words):
    return dict([(word.lower(), True) for word in words])

f = open("tout.txt","r")
lines = f.readlines()
f.close()
count = []
for i in range(11):
  count.append(0)

typedict = {1:"addition" , 2:"reverse" , 3 :"telescopic" , 4:"homophones", 5:"embedded construction" , 6: "multiple definition" , 7:"cryptic definition" , 8:"anagram" , 9:"noncryptic easy" , 10:"general knowledge"}

clues_test = []
clues_train = []
string1 = []
i = 0
while(i<(len(lines)-3)):
	newline = lines[i+1][1:]
	newlines = newline[:-2]
	if (len(newlines) > 2) and (newlines.find(',') != -1):
		num = newlines.split(',')
	else:
		num = newlines
	nums= []
	for x in num:
		
		try:
			zero = int(num[newlines.index(x) + 1])
			num_categ1 = 10
		except:
			num_categ1 = int(x)
		nums.append(num_categ1)
	for x in nums:
		if x == 0:
			continue
		categ = typedict[x]
		if x != 6:
			categ = "something, not charades"
		count[x] += 1
		x1 = (word_feats(lines[i].split()),categ)
		if (x != 2) and (count[x] < 130): 
			clues_train.append(x1)
	i = i + 2
m = 0
for i in clues_train:
	if i[1] == "anagram":
		m = m + 1

print m
print count 

classifier = NaiveBayesClassifier.train(clues_train)
classifier.show_most_informative_features()

f = open("tout1.txt","r")
right = 0
for i in range(0,200):
	line = f.readline()
	line1 = f.readline()
for i in range(0,80):
	line = f.readline()
	line1 = f.readline()
	newline = line1[1:]
	newlines = newline[:-2]
	if (len(newlines) > 2) and (newlines.find(',') != -1):
		num = newlines.split(',')
	else:
		num = newlines
	nums= []
	for x in num:
		try:
			zero = int(num[newlines.index(x) + 1])
			num_categ1 = 10
		except:
			num_categ1 = int(x)
		nums.append(num_categ1)
	n = []
	for l in nums:
		if l != 6:
			n.append("something, not charades")
		else:
			n.append(typedict[l])
	cat = classifier.classify(word_feats(line))
	print cat,n
	try:
		ind = n.index(cat)
		right += 1
	except:
		pass
print right
