
import casesensitive
import upper_lower_symbol_number
print("Enter Choice=1 for casesensetive password that is without capital letters")
print("Enter Choice=2 for upper case,lower case,symbol,number included password")
while True:
    print("")
    c=int(input("Enter your choice:"))
    if(c==1):
        casesensitive.casesensitive()
        break
    elif(c==2):
        upper_lower_symbol_number.upper_lower_symbol_number()
        break
    else:
        print("Invalid choice")
ans=input("Do you want to run again?<y/n>:")
if ans=="n":
    print("")
    sys.exit()

