import nltk
from collections import Counter

test_words = "The Natural Programming Project will study ways to make learning how to program significantly easier. More people will be able to create useful, interesting, and sophisticated programs. The goal is to study how nonprogrammers reason about programming concepts, then to create one or more new programming languages and environments that apply these findings."

tokens = nltk.word_tokenize(test_words)
#print (tokens)
tagged = nltk.pos_tag(tokens)
#print (tagged)
verbs = [word for word,pos in tagged \
	if (pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ' )]
downcased = [x.lower() for x in verbs]
joined = " ".join(downcased).encode('utf-8')
into_string = str(verbs)
print(into_string)
# output = open("output.txt", "w")
# output.write(str(joined))
# output.close()
counts = [Counter(word for word,pos in tagged \
	if (pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ' ))]
print(counts)
