def sumDigits(d):
    total = 0
    for x in str(d):
        total = int(x) + total
    return total

print(sumDigits(3530273294))
print(sumDigits(584))