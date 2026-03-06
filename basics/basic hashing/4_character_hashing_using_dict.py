def character_hashing(c, st):
    d = {}
    for i in st:
        d[i] = d.get(i , 0) + 1
    print(f"frequency of {c} is: {d.get(c , 0)}")

s = input("Enter your sentence: ")
char = input("Enter character you want to check frequency of: ")
character_hashing(char , s)