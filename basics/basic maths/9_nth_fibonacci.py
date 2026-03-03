num = int(input("Enter your number: "))
prev1 = 1
prev2 = 0
if num == 1:
    print(1)
elif num == 0:
    print(0)
else:
    for i in range(2, num+1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
print(prev1)