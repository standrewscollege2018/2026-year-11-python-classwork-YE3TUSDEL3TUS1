playagain=True
while playagain==True:
    import random
    target= random.randint(1,10)
    found=False
    counter=1
    while found==False:
        userinput=int(input("Guess a number from 1 to 10:"))
        if userinput == target:
            found = True
            break
        elif userinput > target:
            print("Too high, try again!")
            counter=counter+1
        elif userinput<target:
            print("Too low, try again!")
            counter=counter+1
    print("Correct!")
    print(f"You took {counter} guesses")
    userinput2=input("Would you like to play again? Type Yes or No")
    bestscore=counter
    if userinput2==("No"):
        playagain=False
    print(f"Your best score is {bestscore}")

