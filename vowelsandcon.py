def vowelorcon(al):
    vowel = 0
    cons = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in al:
        if letter.isalpha():
            if letter in vowels:
                vowel = vowel + 1
            else:
                cons = cons + 1
    print('vowel:' + str(vowel) + ' cons:' + str(cons))
vowelorcon('Mohanlal is a food guy aeiou')
