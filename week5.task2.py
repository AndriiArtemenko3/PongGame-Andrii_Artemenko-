# ceaser cypher 
text = str(input("Phrase:"))
shift = int(input("Shift coefficient:"))
textList = [x for x in text]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in textList:
    if i in alphabet:
        indexing = alphabet.index(i) 
        shiftedIndex = (indexing + shift) % 26 
        print(alphabet[shiftedIndex], end=" ") 
    else:
        print(i, end=" ") 