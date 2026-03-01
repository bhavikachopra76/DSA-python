#121
num = int(input("Enter your number: "))
temp = abs(num)
rev = 0
while temp > 0:
    rem = temp%10
    rev = (rev * 10) + rem
    temp = temp//10

if num == rev:
    print("True")
else:
    print("False")