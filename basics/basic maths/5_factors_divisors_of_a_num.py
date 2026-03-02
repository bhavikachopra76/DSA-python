#9 = [1,3,9]
import math
res = []
num = int(input("Enter your number: "))
print(f"Factors of {num} are: ")
for i in range(1,int(math.isqrt(num))+1):
    if num%i == 0:
        res.append(i)
        if i != num//i:
            res.append(num//i)
print(res)