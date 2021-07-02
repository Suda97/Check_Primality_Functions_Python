def check(num):
    x = 1
    i = 0
    while x <= num:
        if num % x == 0:
            i += 1
        x += 1
    return i


uNum = int(input("Give me number to check: "))

if int(check(uNum)) <= 2:
    print("Prime number!")
else:
    print("Not a prime number!")
