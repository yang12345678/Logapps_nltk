import nltk
from collections import Counter
from nltk.stem import WordNetLemmatizer
import fileinput
from nltk.corpus import treebank

lemmatiser = WordNetLemmatizer()
count = Counter()
final_dict = {}

with open('logapps_appendix.txt', "r") as test_words:
    filestring = str(test_words.read())

def verbage(input_string):
    sent_list = input_string.split('.')
    tag_list = []
    for item in sent_list:
        tokens = nltk.word_tokenize(item )
        tagged = nltk.pos_tag(tokens)
        tag_list.append(tagged)

    printSent(tag_list)
    #print(sent_list)
    #print(tokens)




    verbs = [word for word,pos in tagged \
    	if (pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ' )]

    downcased = [x.lower() for x in verbs]

    joined = " ".join(downcased).encode('utf-8')
    #print str(verbs),'\n'

    listerine = []
    for i in verbs:
        x = (lemmatiser.lemmatize(i, pos="v"))
        listerine.append(x)
    #print str(listerine),'\n'

    for word in listerine:
        count[word] += 1
    #print count,'\n'
    #x = input("Please enter a phrase! ")
    #verbage(x)

def makeDict(tagList):


    for sentence in tagList:
        index = 0
        while ( index < len(sentence)):

            if sentence[index][1] == 'VB' or sentence[index][1] =='VBD' or sentence[index][1] == 'VBG' or sentence[index][1] =='VBN' or sentence[index][1] == 'VBP' or sentence[index][1] =='VBZ':
                 makeString(sentence,index)


            index += 1
            #print(sentence[index][1])
            #print(index)







def printSent(tagList):

    makeDict(tagList)
    for key in final_dict.keys():
        print (key, final_dict[key], '\n')
    x = ''
    while x != 'q':
        x = input(" \n Input the number of the sentence you would like to see or q to quit: ")
        print ("\n",tagList[x])

def makeString(sentence,verb_index):

    string = ''
    string += sentence[verb_index][0] + " "

    index = verb_index + 1
    while index < len(sentence) -1:

        if sentence[index][1] == 'VB' or sentence[index][1] =='VBD' or sentence[index][1] == 'VBG' or sentence[index][1] =='VBN' or sentence[index][1] == 'VBP' or sentence[index][1] =='VBZ' :
            makeString(sentence, index)

        if (sentence[index][1] == 'NN' or sentence[index][1] =='NNS' or sentence[index][1] == 'NNP' or sentence[index][1] =='NNPS') and (sentence[index +1 ][1] == 'RB' or sentence[index +1 ][1] =='RBR' or sentence[index + 1][1] == 'RBS'):
            string += sentence[index][0] + " "
            if sentence[verb_index][0] in final_dict:
                final_dict[sentence[verb_index][0]].append(string)
                return
            else:
                value_list = []
                value_list.append(string)
                final_dict[sentence[verb_index][0]] = value_list
                string = ''
                return




        string += sentence[index][0] + " "
        index += 1

    if sentence[verb_index][0] in final_dict:
        final_dict[sentence[verb_index][0]].append(string)
    else:
        value_list = []
        value_list.append(string)
        final_dict[sentence[verb_index][0]] = value_list

    return





verbage(filestring)
