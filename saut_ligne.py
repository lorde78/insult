phrase = "Hello, pour les nuls, le livre idéal pour la fête de mères"


def Phrase_len(var):
    var2=""
    i = 0
    for f in var:
        var2 += f
        i+=1
        if i == 30:
            var2 +="\n"
    print(i)
    print(var2)
    return i


Phrase_len(phrase)