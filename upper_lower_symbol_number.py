import random
def upper_lower_symbol_number():
    
    char1="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#!$%"
    while 1:
        print("PLEASE ENTER THE DATA BELOW AS NUMBERS")
        password_len=int(input("Length of password?"))
        password_count=int(input("How many password you would like to generate"))
        for x in range(0,password_count):
            password=""
            for x in range(0,password_len):
                password_char=random.choice(char1)
                

                password=password+password_char
            print("Here it is:",password)
        
