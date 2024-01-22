# NATO look-up table 
NATO_table = {
    "a": "alpha", "b": "bravo", "c": "charlie", "d": "delta", "e": "echo", "f": "foxtrot", "g": "golf",
    "h": "hotel", "i": "india", "j": "juliett", "k": "kilo", "l": "lima", "m": "mike", "n": "november",
    "o": "oscar","p": "papa", "q": "quebec", "r": "romeo", "s": "sierra", "t":"tango", "u": "uniform", 
    "v": "victor", "w": "whiskey", "x": "xray", "y": "yankee", "z": "zulu" 
}

text = str(input("Provide a word:"))

for i in text: #each character of the word is now printed word-by-word based on NATO lookup table
    word = NATO_table.get(i)
    print(word)

convert = [NATO_table.get(char, char) for char in text]