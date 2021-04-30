def verif(returned_sentence,mot):
    i = 0
    alors = "z"
    while i < len(Pcat1):
        if Pcat1[i] == returned_sentence:
            alors = "a"
        else:
            if Pcat2[i] == returned_sentence:
                alors = "b"
            else:
                if Pcat3[i] == returned_sentence:
                    alors = "c"
        i += 1
    print(alors)
    j = 0
    donc = "y"
    while j < len(Mcat1):
        if Mcat1[j] == mot:
            donc = "d"
        j += 1
    if donc == "y":    
        k = 0
        while k < len(Mcat2):
            if Mcat2[k] == mot:
                donc == "e"
            k += 1        
    if donc == "y":
        l = 0
        while l < len(Mcat3):
            if Mcat3[l] == mot:
                donc = "f"
            l += 1

verif = verif(returned_sentence, returned_word)


print(verif)