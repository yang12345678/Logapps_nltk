import nltk
from collections import Counter
from nltk.stem import WordNetLemmatizer
import fileinput
from nltk.corpus import treebank

lemmatiser = WordNetLemmatizer()

verb_list = []
object_list = []
sentence_number = []
paragraph_number = []

with open('logapps_appendix.txt', "r") as test_words:
    filestring = str(test_words.read())

def verbage(input_string):

    sent_list = input_string.split('.')
    tag_list = []
    for item in sent_list:
        tokens = nltk.word_tokenize(item )
        tagged = nltk.pos_tag(tokens)
        tag_list.append(tagged)
    makeDict(tag_list)
    return verb_list, object_list, sentence_number, paragraph_number




def makeDict(tagList):

    paragraph_num = 1
    sent_num = 1
    for sentence in tagList:

        if sent_num == 4:
            paragraph_num = 2
        elif sent_num >= 5:
            paragraph_num = 3
        index = 0
        while ( index < len(sentence)-1):

            if sentence[index][1] == 'IN':
                index += 2

            x = (lemmatiser.lemmatize(sentence[index][0] , pos="v"))
            if x == "be":
                index +=1

            if sentence[index][1] == 'VB' or sentence[index][1] =='VBD' or sentence[index][1] == 'VBG' or sentence[index][1] =='VBN' or sentence[index][1] == 'VBP' or sentence[index][1] =='VBZ':

                makeLists(sentence,index,sent_num,paragraph_num)



            index += 1
        sent_num +=1



def printSent(tagList):


    # for key in final_dict.keys():
    #     print (key, final_dict[key], '\n')
    #
    # x = getKeys(final_dict)
    # print(x)
    pass

def getKeys(dictionary):

    return dictionary.keys()

def makeLists(sentence,verb_index,sent_num,paragraph_num):

    string = ' '

    index = verb_index + 1
    while index < len(sentence) :

        #if there is a noun followed by an adverb
        if index != len(sentence)-1:

            if (sentence[index][1] == 'NN' or sentence[index][1] =='NNS' or sentence[index][1] == 'NNP' or sentence[index][1] =='NNPS') and (sentence[index +1 ][1] == 'RB' or sentence[index +1 ][1] =='RBR' or sentence[index + 1][1] == 'RBS'):
                string += sentence[index][0] + " "

                x = (lemmatiser.lemmatize(sentence[verb_index][0] , pos="v"))

                verb_list.append(x)
                object_list.append(string)
                sentence_number.append(sent_num)
                paragraph_number.append(paragraph_num)
                return


            #if there is punctuation or adjectives skip over them
            while (sentence[index][1] == 'JJ' or sentence[index][1] =='JJR' or sentence[index][1] == 'JJS' or sentence[index][1] == ',' or sentence[index][1] =='.' or sentence[index][1] == ':' or sentence[index][1] == 'CC' ):
                index += 1





        string += sentence[index][0] + " "
        index += 1

    x = (lemmatiser.lemmatize(sentence[verb_index][0] , pos="v"))
    verb_list.append(x)
    object_list.append(string)
    sentence_number.append(sent_num)
    paragraph_number.append(paragraph_num)

    return

def give_variables():
    x = verb_list
    return x

def ygive_variables():
    y = object_list
    return y

def zgive_variables():
    z = sentence_number
    return z

def wgive_variables():
    w = paragraph_number
    return w


verbage(filestring)
