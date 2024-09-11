def temp_conversion(celsius):

    return fahrenheit

if __name__ == '__main__':
    celsius = 0.0
    fahrenheit = 0.0

    celsius = float(input("Enter a Celsius temperature: "))

    fahrenheit = (9 / 5) * celsius + 32

    print ("That is equal to", format(fahrenheit, '.2f'), "degrees Fahrenheit.")
temp_conversion(celsius)
