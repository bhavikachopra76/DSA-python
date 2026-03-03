def print_nums(start, n):
    if start > n:
        return
    print_nums(start + 1, n)
    print(start , end = " ")

num = int(input("Enter your number: "))
print_nums(1,num)