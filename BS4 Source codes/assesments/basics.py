choise = int(input("C- convert from fahrenheit to celsis\nF-convert from celsis to fahrenheit\nEnter your choice(1/2): "))
if choise == 1:
    f = float(input("Enter the temperature in Fahrenheit:"))
    c = (f-32)*5/9
    print("Temperature in Celsius: ",round(c))
    
elif choise == 2:
    c = float(input("Enter the temperature in Celsius:"))
    f = (c*9)/5+32
    print("Temperature in Fahrenheit: ",round(f)) 

else:
    print("Please choose the correct option.")