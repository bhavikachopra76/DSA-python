"""
Euclidean Algorithm
gcd(a,b) = gcd(b, a%b)
when 'b' becomes zero 'a' is the answer
"""
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

while num2 != 0:
    num1 , num2 = num2 , num1%num2

print(num1)