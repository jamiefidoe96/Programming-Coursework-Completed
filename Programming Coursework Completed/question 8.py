
def vowelRemoval(string):
    VOWELS = ("a", "e", "i", "o", "u")
    if len(string) == 0:
        return string
    else:
        newString = string[1:len(string) + 1]
        firstLetter = string[0]
        
        if firstLetter in VOWELS:

            return vowelRemoval(newString)
        else:
            return firstLetter + vowelRemoval(newString)
