# assignment: PA2-Vending Machine
# author: Aradhya Kapoor
# date: 10/25/23
# file: Implement a vending machine that will ask user to buy something and give change after buying.  
# input: strings and numbers (integers)
# output:interactive messages strings


print("Vending Machine") 
y = "Please enter what product you want to buy[1-3] or select quit[4]: \n1.A bottle of water - $1.99 \n2.A bottle of orange juice - $2.15 \n3.A bottle of iced tea - $2.49 \n4.Quit"
while True: 
    print(y)
    x = str(input(""))

    if x == '1':
        price = int(input("Please deposit money (in cents): \n"))
        while(price < 199):
            price += int(input("Please deposit money (in cents): \n"))
        change =  price - 199
        dollars = change // 100  
        change = change % 100     
        quarters = change // 25 
        change = change % 25
        dimes = change // 10
        change = change % 10
        nickels = change // 5
        change = change % 5
        cents = change
    
        print("You bought a bottle of water.")
        if(dollars + quarters + dimes + nickels + cents != 0):
            print("Your change is:")           
            if dollars != 0:
                print(f"Dollars - {dollars}")
            if quarters != 0:
                print(f"Quarters - {quarters}")
            if dimes != 0:
                print(f"Dimes - {dimes}")
            if nickels != 0:
                print(f"Nickels - {nickels}")
            if cents != 0:
                print(f"Cents - {cents}")

    elif x == '2':
        price = int(input("Please deposit money (in cents): \n"))
        while(price < 215):
            price += int(input("Please deposit money (in cents): \n"))
        change =  price - 215
        dollars = change // 100  
        change = change % 100     
        quarters = change // 25 
        change = change % 25
        dimes = change // 10
        change = change % 10
        nickels = change // 5
        change = change % 5
        cents = change
    
        print("You bought a bottle of orange juice.")
        if(dollars + quarters + dimes + nickels + cents != 0):
            print("Your change is:")           
        if dollars != 0:
            print(f"Dollars - {dollars}")
        if quarters != 0:
            print(f"Quarters - {quarters}")
        if dimes != 0:
            print(f"Dimes - {dimes}")
        if nickels != 0:
            print(f"Nickels - {nickels}")
        if cents != 0:
            print(f"Cents - {cents}")

    elif x == '3':
        price = int(input("Please deposit money (in cents): \n"))
        while(price < 249):
            price += int(input("Please deposit money (in cents): \n"))
        change =  price - 249
        dollars = change // 100  
        change = change % 100     
        quarters = change // 25 
        change = change % 25
        dimes = change // 10
        change = change % 10
        nickels = change // 5
        change = change % 5
        cents = change
    
        print("You bought a bottle of iced tea.")
        if(dollars + quarters + dimes + nickels + cents != 0):
            print("Your change is:")           
        if dollars != 0:
            print(f"Dollars - {dollars}")
        if quarters != 0:
            print(f"Quarters - {quarters}")
        if dimes != 0:
            print(f"Dimes - {dimes}")
        if nickels != 0:
            print(f"Nickels - {nickels}")
        if cents != 0:
            print(f"Cents - {cents}")

    elif x == '4':
        print("Goodbye!")
        break
    else:
        print("You made the wrong choice!")


