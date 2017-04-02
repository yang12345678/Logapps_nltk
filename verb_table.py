import nltk_verb
import texttable as tt
with open('logapps_appendix.txt', "r") as goodtest_words:
    filestring = str(goodtest_words.read())
tab = tt.Texttable()
bat = tt.Texttable()
varb = nltk_verb.give_variables()
varb2 = nltk_verb.ygive_variables()
varb3 = nltk_verb.zgive_variables()
varb4 = nltk_verb.wgive_variables()
print(varb)
# print (varb)
# bat = tt.Texttable()
# print(verb_list)

header = ['Para. #', 'Sent. #', "Verb", "Object"]
tab.header(header)

for i in range(len(varb) - 1):
    row = [varb4[i],varb3[i],varb[i],varb2[i]]
    tab.add_row(row)


header2 = nltk_verb.give_variables()
header2.insert(0, " ")
bat.header(header2)
print(len(header2))
for i in range(len(varb) - 1):
    row = ["None"] * (len(varb))
    row[0] = varb2[i]
    row[i + 1] = "1"
    bat.add_row(row)



s = tab.draw()
t = bat.draw()
print(s)
print(t)


text_file = open("table1.txt", "w")
text_file.write(s)
text_file.close()

text_file = open("table2.txt", "w")
text_file.write(t)
text_file.close()
