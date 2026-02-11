'''Calculate dosage of drugs'''

age=int(input("What is your age?"))
weight=int(input("What is your weight?"))
if age<=11: 
    if 50>weight>25:
        print(f"Take {weight*10} mg paracetamol")
    else: print("You are at an unhealthy weight")
elif 100<weight or 35>weight: print("You are at an unhealthy weight")
else: print("Take 1000 mg paracetamol (2 tablets)")