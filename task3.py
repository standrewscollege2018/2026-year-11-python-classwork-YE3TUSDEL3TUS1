total = 0 
while total <= 200:
        num = int(input("Enter a number between 50 and 100: "))
        if num < 50 or num > 100:
            print("Number must be between 50 and 100. Try again.")
        else: total+=num
        print(f"Current total: {total}")
print(f"Final total is {total}, which is greater than 200.")