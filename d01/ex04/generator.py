import time


def generator(txt, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    if (not isinstance(txt, str) or
            (not isinstance(option, str) and option is not None)
            and (option != "shuffle" and option != "unique" and option != "ordered")):
        print("ERROR")
        return
    i = 0
    rd_lst = []
    lst = txt.split(sep)
    if (option == "ordered"):
        lst.sort(key=str.lower)
    elif (option == "shuffle"):
        rd = int(round(time.time()*10000)) % (len(lst))
        size = len(lst)
        while (i < size):
            rd_lst.append(lst[rd])
            del lst[rd]
            if (len(lst) > 0):
                rd = int(round(time.time()*10000)) % (len(lst))
            i += 1
        lst = rd_lst
    elif (option == "unique"):
        lst = list(set(lst))

    for i in lst:
        yield(i)


text = "Salut comment allez vous par ici ? ici comment"
for word in generator(text, " ", "shuffle"):
    print(word)
