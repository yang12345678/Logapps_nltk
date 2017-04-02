import nltk
from collections import Counter
from nltk.stem import WordNetLemmatizer
import fileinput
import sys
from nltk.corpus import treebank
count = Counter()
lemmatiser = WordNetLemmatizer()
count = Counter()
final_dict = {}

with open('logapps_appendix.txt', "r") as test_words:
    filestring = str(test_words.read())

def verbage(input_string):
    sent_list = input_string.split('.')
    tag_list = []
    rokens = nltk.word_tokenize(input_string)
    ragged = nltk.pos_tag(rokens)
    for item in sent_list:
        tokens = nltk.word_tokenize(item)
        tagged = nltk.pos_tag(tokens)
        tag_list.append(tagged)

    makeDict(tag_list)
    printSent(tag_list)

    verbs = [word for word,pos in ragged \
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


def makeDict(tagList):


    for sentence in tagList:
        index = 0
        while ( index < len(sentence)):


            x = (lemmatiser.lemmatize(sentence[index][0] , pos="v"))
            if x == "be":
                index +=1

            if sentence[index][1] == 'IN':
                index += 2

            if sentence[index][1] == 'VB' or sentence[index][1] =='VBD' or sentence[index][1] == 'VBG' or sentence[index][1] =='VBN' or sentence[index][1] == 'VBP' or sentence[index][1] =='VBZ':

                makeString(sentence,index)
                # print(sentence[index][1])



            index += 1

            #print(sentence[index][1])
            #print(index)



def printSent(tagList):


    # for key in final_dict.keys():
    #     print (key, final_dict[key], '\n')
    # x = ''
    # while x != -1:
    #     x = input(" \n Input the number of the sentence you would like to see or -1 to quit: ")
    #     print ("\n",tagList[int(x)])
    # return key
    pass

def makeString(sentence,verb_index):

    string = ' '

    index = verb_index + 1
    while index < len(sentence) -1:

        #if there is a noun followed by an adverb
        if (sentence[index][1] == 'NN' or sentence[index][1] =='NNS' or sentence[index][1] == 'NNP' or sentence[index][1] =='NNPS') and (sentence[index +1 ][1] == 'RB' or sentence[index +1 ][1] =='RBR' or sentence[index + 1][1] == 'RBS'):
            string += sentence[index][0] + " "

            x = (lemmatiser.lemmatize(sentence[verb_index][0] , pos="v"))
            if x in final_dict:
                final_dict[sentence[verb_index][0]].append(string)
                return
            else:
                value_list = []
                value_list.append(string)
                final_dict[x] = value_list
                string = ' '
                return

        #if there is punctuation or adjectives skip over them
        while (sentence[index][1] == 'JJ' or sentence[index][1] =='JJR' or sentence[index][1] == 'JJS' or sentence[index][1] == ',' or sentence[index][1] =='.' or sentence[index][1] == ':' or sentence[index][1] == 'CC' ):
            index += 1





        string += sentence[index][0] + " "
        index += 1

    x = (lemmatiser.lemmatize(sentence[verb_index][0] , pos="v"))
    if x in final_dict:

        final_dict[x].append(string)
    else:
        value_list = []
        value_list.append(string)
        final_dict[x] = value_list

    return

if __name__ == '__main__':
    a = (verbage(filestring))
