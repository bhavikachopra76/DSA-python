def print_num(current, stop):
    if current > stop:
        return
    print(current , end = " ")
    print_num(current + 1, stop)

num = int(input("Enter your number: "))
print_num(1,num)


