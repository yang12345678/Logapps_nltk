import nltk
from collections import Counter
from nltk.stem import WordNetLemmatizer
import fileinput
lemmatiser = WordNetLemmatizer()
count = Counter()

with open('logapps_appendix.txt', "r") as test_words:
    filestring = str(test_words.read())

def verbage(input_string):
    tokens = nltk.word_tokenize(input_string)
    tagged = nltk.pos_tag(tokens)

    verbs = [word for word,pos in tagged \
    	if (pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ' )]
    downcased = [x.lower() for x in verbs]
    joined = " ".join(downcased).encode('utf-8')
    print(str(verbs))

    listerine = []
    for i in verbs:
        x = (lemmatiser.lemmatize(i, pos="v"))
        listerine.append(x)
    print(str(listerine))

    for word in listerine:
        count[word] += 1
    print(count)
    x = input("Please enter a phrase! ")
    verbage(x)

print(verbage(filestring))
