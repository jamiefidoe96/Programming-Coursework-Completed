def reverse_word(txt):
    reverse = " "
    string = " "
    for char in txt:
        if char != " ":
            string += char
        else:
            reverse = string + " " + reverse
            string = " "

    reverse = string + " " + reverse
    txt = reverse
    return txt

            


