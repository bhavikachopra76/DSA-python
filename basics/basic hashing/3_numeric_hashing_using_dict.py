def numeric_hashing(number, lt):
    d = {}
    for x in range(len(lt)):
        d[lt[x]] = d.get(lt[x] , 0) + 1
    print(f"frequency of {number} is: {d.get(number , 0)}")

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    lst.append(int(input()))

num = int(input("Enter element you want to check frequency of: "))
numeric_hashing(num, lst)