def text_analyzer(txt=None):
    upper = 0
    lower = 0
    space = 0
    punct = 0
    if (txt is None):
        print("what is the text to analyze ?")
        txt = input()
    if (txt == ""):
        print("This function counts the number of upper characters, \
lower characters, punctuation and spaces in a given text.")
        return
    else:
        for i in range(0, len(txt)):
            if (txt[i].isupper()):
                upper += 1
            elif (txt[i].islower()):
                lower += 1
            elif (txt[i] == " "):
                space += 1
            else:
                punct += 1
    print("The text contains", (upper + lower + punct + space), "characters:\n\
    -", upper, "upper letters\n\
    -", lower, "lower letters\n\
    -", punct, "punctuation marks\n\
    -", space, "spaces")
