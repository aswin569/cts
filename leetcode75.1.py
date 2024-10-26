word1 = input()
word2 = input()
if (len(word1)< len(word2)):
    l = len(word1)
else:
    l = len(word2)

rword = ""
for i in range(0,l):
    rword += word1[i]
    rword += word2[i]
rword +=word1[l:]
rword +=word2[l:]
print(rword)