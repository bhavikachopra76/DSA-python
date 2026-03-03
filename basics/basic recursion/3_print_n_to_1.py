def print_nums(n):
    if n < 1:
        return
    print(n , end = " ")
    print_nums(n-1)

num = int(input("Enter your number: "))
print_nums(num)
