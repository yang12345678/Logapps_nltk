import nltk
from collections import Counter
from nltk.stem import WordNetLemmatizer
import fileinput
import sys
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
    # print (str(verbs))

    listerine = []
    for i in verbs:
        x = (lemmatiser.lemmatize(i, pos="v"))
        listerine.append(x)

    print(str(listerine))
    return listerine

def verbwork(array):
    listerine = array
    x, y = input("Want to replace some verb?\nType in the one to replace and the one you want.\nOtherwise, enter '0 0'. ").split(" ")
    if x != 0:
        for j in range(len(listerine)-1):
            if listerine[j] == x:
                listerine[j] = y
        # print (str(listerine) + "\n")
    else:
        pass

    for word in listerine:
        count[word] += 1
    print(count)


    z = input("Please enter a phrase or press 0 to exit. ")
    if z == "0":
        sys.exit()
    else:
        verbage(z)

a = (verbage(filestring))
print(verbwork(a))
