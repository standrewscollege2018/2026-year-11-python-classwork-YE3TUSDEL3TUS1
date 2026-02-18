numberlist = [2, 4, 7, 11, 15]
target = int(input("Enter a number: "))
found = False                   
if any(x + y == target and x != y for x in numberlist for y in numberlist):
        if x + y == target and x != y:
            found = True
            break                                 
if found:
    print("Yes, the number can be formed")
else:
    print("No, the number cannot be formed")