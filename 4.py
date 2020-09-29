n = abs(int(input("Insert a whole positive number ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Max numeral in a number is a", max)
        break