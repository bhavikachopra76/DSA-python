num = int(input("Enter a number: "))
length = 0
temp = num
while temp > 0:
    length = length + 1
    temp = temp//10

print(f"No. of digits in {num} are : {length}")
