userinput=int(input("Enter a number"))
x=False
while x==False:
    userinput2=int(input("Enter another number, your first number was too small"))
    if userinput2>userinput:
        x=True
if x==True:
    print(f"You entered {userinput} and {userinput2}")

    