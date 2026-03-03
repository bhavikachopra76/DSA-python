def print_nums(current, n):
    if current < 1:
        return
    print_nums(current - 1, n)
    print(current , end = " ")

num = int(input("Enter your number: "))
print_nums(num,num)