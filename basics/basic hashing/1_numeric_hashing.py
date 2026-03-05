def check_frequency(number , l):
    lt = [0] * 10**6
    for x in range(len(l)):
        lt[l[x]] = lt[l[x]] + 1
    print(f"frequency of {number} is: {lt[number]}")

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    lst.append(int(input()))

num = int(input("Enter element you want to check frequency of: "))
check_frequency(num, lst)
