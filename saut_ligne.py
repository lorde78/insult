
def Phrase_len(var):
    var2=""
    i = 0
    for f in var:
        var2 += f
        i+=1
        if i > 28 and f == " ":
            var2 +="\n"
            i = -10
    print(var2)
    return var2
