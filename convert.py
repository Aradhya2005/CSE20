# assignment: PA3-Converter
# author: Aradhya Kapoor
# date: 11/06/23
# file: Implement that emulates a simple SI unit conversion calculator that can convert Fahrenheit into Celsius, miles to kilometers (km), and pounds into kilograms (kg).
# input: strings and numbers (integers)
# output:interactive messages strings

print("Welcome to the SI Unit Converter!")
    
def format ( num, precision = 2):
        if round(num, 2) == round(num):
                return round(num)
        else:
                return round(num, 2)
def isfloat(token):
        return token.replace(".", "").isnumeric()

        
def fahrenheit_celsius ():
        print(f"{original} Fahrenheit corresponds to {convert} Celsius.")
            
def miles_km ():
        print(f"{original} miles corresponds to {convert} km.")
def pounds_kg():
        print(f"{original} pounds corresponds to {convert} kg.")
def job(choice):
        return choice == 'F' or choice == 'f' or choice == 'p' or choice == 'P' or choice == 'M' or choice ==  'm'
        
        

y = "Please choose one of the following conversions: \nFahrenheit to Celsius - F \nPounds to kg - P \nMiles to km - M\n"
work = input(y)

while job(work) == False:
        work = input('You did not choose correctly.\n' + (y))

while True:
        if job(work) == False:
                work = input('You did not choose correctly.\n' + (y))
        if work == "F" or work == "f":
                original = input("Please enter a temperature in Fahrenheit:\n")
                while isfloat(original) == False:
                        print("You did not enter a number.")
                        original = input("Please enter a temperature in Fahrenheit:\n")
                if format(float(original)) == float(original):
                        original = format(float(original))
                convert = format(((float(original) - 32) * 5 / 9))
                fahrenheit_celsius()
        elif work == "P" or work == "p":
                original = input("Please enter pounds:\n")
                while isfloat(original) == False:
                        print("You did not enter a number.")
                        original = input("Please enter pounds:\n")
                if format(float(original)) == float(original):
                        original = format(float(original))
                convert = format((float(original) * 0.45359237))
                pounds_kg()
        elif work == "M" or work == "m":
                original = input("Please enter miles:\n")
                while isfloat(original) == False:
                        print("You did not enter a number.")
                        original = input("Please enter miles:\n")
                if format(float(original)) == float(original):
                        original = format(float(original))
                convert = format((float(original) * 1.609344))
                miles_km()
        z = input("Do you want to continue? [Y/N]:\n")
        if z != "Y" and z != "y":
                print("Goodbye!")
                break
        else:
                work = input(y)
        
        
        
                                
                        

    
    
    



    

    
        
                        
                
    
            
        
        
        
        
       
