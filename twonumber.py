userinput=int(input("Enter a number"))
userinput2=int(input("Enter another number"))
if userinput == userinput2:
    print(f"You entered {userinput} and {userinput2}, which adds to {userinput+userinput2}. These two numbers are equal")
elif userinput>userinput2:
    print(f"You entered {userinput} and {userinput2}, which adds to {userinput+userinput2}. {userinput} is greater than {userinput2}")
else: print(f"You entered {userinput} and {userinput2}, which adds to {userinput+userinput2}. {userinput2} is greater than {userinput2}")