CHILD_AGE=13
user_input=int(input("What is your age?"))
if user_input<=CHILD_AGE:
    print("You pay the child price!")
    
elif user_input>=CHILD_AGE:
    print("You pay the full price!")
print("Welcome to the zoo.")