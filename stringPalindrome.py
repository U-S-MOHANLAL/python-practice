def checkPalindrome(word):
    rev = ''
    for letter in word:
        rev = letter + rev
    if rev == word:
        print("It's palindrome word")
    else:
        print("It's not a palindrome word")    
checkPalindrome('lal')