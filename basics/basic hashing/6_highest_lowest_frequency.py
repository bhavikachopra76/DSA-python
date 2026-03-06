def count_frequency(lt):
    d = {}
    for x in lt:
        d[x] = d.get(x , 0) + 1

    print(f"Highest frequency is of number: {max(d , key = d.get)} and lowest frequency is of number: {min(d, key = d.get)} ")

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    lst.append(int(input()))
count_frequency(lst)