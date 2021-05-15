
def Phrase_len(var):
    var2=""
    i = 0
    unefois = False
    for f in var:
        var2 += f
        i+=1
        if i > 26 and f == " " and unefois == False:
            var2 +="\n"
            unefois = True
    
    print(var2)
    return var2
