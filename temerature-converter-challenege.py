def celsius_to_fahrenheit(celsius):
    return (celsius*9/5)+32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

def celsius_to_kelvin(celsius):
    return celsius+273.15
 
def kelvin_to_celsius(kelvin):
    return kelvin-273.15

def menu():
    print("What would you like to convert?")
    print("(1)celsius to fahrenheit")
    print("(2)fahrenheit to celsius")
    print("(3)Kelvin to or celsius")
    print("(4)celsius to kelvin")
    print("(5)quit")
def main():
    loop=1
    choice=0

    while loop==1:
        menu()
        choice=eval(input("Choose what you want to convert"))

        if choice==1:
            celsius=eval(input("Enter temp"))
            print(celsius_to_fahrenheit(celsius))
        elif choice==2:
            fahrenheit=eval(input("Enter temp"))
            print(fahrenheit_to_celsius(fahrenheit))
        elif choice==3:
          kelvin=eval(input("Enter temp"))
          print(kelvin_to_celsius(kelvin))
        elif choice==4:
          celsius=eval(input("Enter temp"))
          print(celsius_to_kelvin(celsius))
        elif choice==5:
          print("thank you for using my converter ")
          loop=0

main()

