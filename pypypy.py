#n=[2,1,1,4,7,11,15];target=int(input("Enter a number: "));print("Yes, the number can be made"if any(x+y==target for x in n for y in n if x!=y)else"No, the number cannot be made")
#use above with all values distinct
n=[1,1,2,4,7,11,15];userinput=int(input("Enter a number: "));print("Yes, the number can be made"if any(n[i]+n[j]==userinput for i in range(len(n))for j in range(i+1,len(n)))else"No, the number cannot be made")
#use second above for some values non-distinct