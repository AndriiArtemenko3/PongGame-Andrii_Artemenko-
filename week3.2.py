def pig_latin_converter(word):
    vowels = "aeiouAEIOU" # our dict for vowels
    
    if word[0] in vowels:
        pig_latin_word = word + "way"
    else: 
        first_vowel_index = None

    for letter in word:
        if letter in vowels:
            first_vowel_index = word.index(letter)
            break

    if first_vowel_index is not None:
            pig_latin_word = word[first_vowel_index:] + word[:first_vowel_index] + "ay"
    else:
            pig_latin_word = word + "ay"

    return pig_latin_word

eng_word = input("Provide english word:")

pig_latin_result = pig_latin_converter(eng_word)
print("Pig Latin:", pig_latin_result)