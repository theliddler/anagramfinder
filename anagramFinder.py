def toString(List):
    listasstring = ''
    for s in List:
        listasstring += s + " "
    return listasstring
 
def findAnagrams(word):
    f = open('english.txt', 'r')

    wordlen = len(word)
    sortedword = ''.join(sorted(word))

    anagrams  = []
    
    for dirword in f.read().split():
        sorteddirword = ''.join(sorted(dirword))
        if (sortedword == sorteddirword) and (wordlen == len(dirword)):
            anagrams.append(dirword)

    return toString(anagrams)

word = input("Insert string: ")
words = findAnagrams(word)
if words:
    print ("Anagrams: " + words)
else:
    print ("I couldn't find any anagrams.")
