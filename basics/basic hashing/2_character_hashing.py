def check_frequency(c , st):
    cleaned = st.replace(" ", "")
    lst = [0] * 256
    for i in range(len(cleaned)):
        idx = ord(cleaned[i])
        lst[idx] = lst[idx] + 1

    print(f"frequency of {c} is: {lst[ord(c)]}")

string = input("Enter sentence: ")
char = input("Enter character you want to check frequency of: ")
check_frequency(char, string)