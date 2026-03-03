def reverse_arr(l , pt1 , pt2):
    if pt1 > pt2:
        return
    l[pt1] , l[pt2] = l[pt2] , l[pt1]
    reverse_arr(l , pt1 + 1, pt2 - 1)

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    num = int(input())
    lst.append(num)
reverse_arr(lst , 0 , len(lst)-1)
print(lst)
