# import nltk_verb.verbage
import texttable as tt
tab = tt.Texttable()


header = ['Para. #', 'Sent. #', "Verb", "Object"]
tab.header(header)
row = ["1", "1", "study", "ways to make learning how to program"]
tab.add_row(row)

# with open('logapps_appendix.txt', "r") as goodtest_words:
#     filestring = str(goodtest_words.read())

s = tab.draw()
print(s)
