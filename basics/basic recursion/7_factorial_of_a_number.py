def fact(n):
    if n == 0:
        return 1
    mul = fact(n - 1)
    mul = mul * n
    return mul

num = int(input("Enter your number: "))
print(f"factorial of {num} is {fact(num)}")