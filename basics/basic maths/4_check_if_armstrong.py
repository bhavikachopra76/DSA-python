#153
num = int(input("Enter your number: "))
length = len(str(num))

add = 0
temp = num
while temp > 0:
    rem = temp % 10
    add = add + (rem**length)
    temp = temp//10

if add == num:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")