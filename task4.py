userinput=input("Enter a barcode")
countrycode= userinput[:2]
manufacturercode=userinput[2:7]
productcode=userinput[7:12]
checkdigit=userinput[12]
if len(userinput) != 13:
    print("Barcode is not 13 digits, try again")
else: print(f"Countrycode={countrycode}, Manufacturercode={manufacturercode}, Product={productcode},Last digit={checkdigit}")
    