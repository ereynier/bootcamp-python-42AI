languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

s = ""

for i in languages:
    s += "{}".format(i)
    s += " was created by "
    s += "{}".format(languages[i])
    s += "\n"
print(s)
