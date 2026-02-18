for num in range (40):
    if num % 5 == 0 or num % 3 == 0:
        if num % 3 == 0:
            print ("Fizz")
        if num % 5 == 0:
            print("Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print ("FizzBuzz")
    else: 
        print (num)
    