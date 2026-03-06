def count_frequency(lt):
    d = {}
    for x in lt:
        d[x] = d.get(x , 0) + 1

    for key in d:
        print(f"Frequency of {key} is {d.get(key)}")

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    lst.append(int(input()))
count_frequency(lst)