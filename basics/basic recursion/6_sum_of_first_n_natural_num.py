def print_sum(n):
    if n < 1:
        return 0
    add = print_sum(n - 1)
    add = add + n
    return add

num = int(input("Enter your number: "))
print(f"Sum of {num} natural no.'s is {print_sum(num)}")
