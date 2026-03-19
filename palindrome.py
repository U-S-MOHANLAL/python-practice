def checkPalindrome(n):
    number = n
    reversed = 0
    while number != 0:
        rem = number % 10
        number = number//10
        reversed = reversed * 10 + rem
    print(reversed)
    if reversed == n:
        print("It's palindrome")
    else: 
        print("It's not a palindrome")
checkPalindrome(5335)