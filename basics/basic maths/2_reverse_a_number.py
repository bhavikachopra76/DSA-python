#1234
#4321

num = int(input("Enter your number: "))
temp = abs(num)
rev = 0
while temp > 0:
    rem = temp%10
    rev = (rev * 10) + rem
    temp = temp//10

if num < 0:
    print(f"Reverse of {num} is {rev*-1}")
else:
    print(f"Reverse of {num} is {rev}")