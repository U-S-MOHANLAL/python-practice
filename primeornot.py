def checkPrimeOrNot(n):
    if n <=1 :
        return 'yes'
    i = n - 1
    while i != 2:
        if n % i == 0:
            return 'No'
        i = i-1
    return 'yes'

print(checkPrimeOrNot(31))
print(checkPrimeOrNot(4))
print(checkPrimeOrNot(6))
print(checkPrimeOrNot(7))
print(checkPrimeOrNot(54))