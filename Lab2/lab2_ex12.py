def rhyme(words_list):
    result = []

    for index in range(len(words_list)): # -1
        rhymes_with = ()
        for j in range(index + 1, len(words_list)):
            if words_list[index][-2:] == words_list[j][-2:]:
                rhymes_with = rhymes_with + (words_list[j],)
        if rhymes_with:
            list = [words_list[index], rhymes_with]
            result.append(list)
    
    return result

l = ['ana', 'banana', 'carte', 'arme', 'parte']
print(rhyme(l))