s = input("Enter your sentence: ")
cleaned = "".join(char.lower() for char in s if char.isalnum())
if cleaned[::-1] == cleaned:
    print("valid")
else:
    print("not valid")