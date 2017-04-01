import nltk_verb
import texttable as tt
with open('logapps_appendix.txt', "r") as goodtest_words:
    filestring = str(goodtest_words.read())
tab = tt.Texttable()
bat = tt.Texttable()
varb = nltk_verb.verbage(filestring)

header = ['Para. #', 'Sent. #', "Verb", "Object"]
tab.header(header)
for i in varb:
    row = ["1", "1", i, "ways to make learning how to program"]
    tab.add_row(row)

header2 = ['Object Placeholder', 'Object Placeholder', "Object Placeholder", "Object Placeholder"]
for j in varb:
    row = [i, "VIRUS", "BACTERIA", "PARASITE"]
tab.header(header)


s = tab.draw()
t = bat.draw()
print(s)
print(t)
