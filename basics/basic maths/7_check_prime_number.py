import math
num = int(input("Enter your number: "))

if num <= 1:
    print(f"{num} is not a prime number")
else:
    flag = True
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            flag = False
            break

    if not flag:
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number")
