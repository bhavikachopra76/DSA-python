def name_print(user_name, n, count):
    if count == n:
        return
    print(f"My name is {user_name}")
    name_print(user_name , n , count+1)



name = input("Enter your name: ")
num = int(input("Enter number of times you want to print: "))
name_print(name, num , 0)