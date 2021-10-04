y = "00000happybirthday000"
y=y.strip("0")
print(y)

string = "supercalifrag"
print(string[5:9:1])
print(string[5::2])
print(string[:5])
print(string[::-1])
print(string[-2])
print(string[string.index("cali"):string.index("frag")])


word = "antidisestablishmentarianism"

answer = word[word.index("establishment"):word.index("establishment")+len("establishment")]

print(answer)