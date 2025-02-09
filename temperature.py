def celsius_to_fahren(degrees):
    return (9/5 * degrees) + 32

def celsius_to_kelvin(degrees):
    return degrees + 273

def fahren_to_celsius(degrees):
    return (degrees - 32) * 5/9

def fahren_to_kelvin(degrees):
    celsius_conversion = fahren_to_celsius(degrees)
    return celsius_to_kelvin(celsius_conversion)

def kelvin_to_celsius(degrees):
    return degrees - 273

def kelvin_to_fahren(degrees):
    celsius_conversion = kelvin_to_celsius(degrees)
    return celsius_to_fahren(celsius_conversion)

def main():
    
    print("—> Conversión de temperatura <—")

    print("\nSelecciona una conversión:\n0: Salir\n1: °C a °F\n2: °C a K\n3: °F a °C\n4: °F a K\n5: K a °C\n6: K a °F\n")

    while True:

        user_option = int(input("Opción: "))

        if user_option == 0:

            print(f"\n¡Hasta pronto!")

            break

        elif user_option == 1:

            user_degrees = int(input("\nGrados Celsius: "))

            fahren = celsius_to_fahren(user_degrees)

            print(f"\n{user_degrees} °C es equivalente a {fahren} °F.\n")

        elif user_option == 2:

            user_degrees = int(input("\nGrados Celsius: "))

            kelvin = celsius_to_kelvin(user_degrees)

            print(f"\n{user_degrees} °C es equivalente a {kelvin} K.\n")

        elif user_option == 3:

            user_degrees = int(input("\nGrados Fahrenheit: "))

            celsius = fahren_to_celsius(user_degrees)

            print(f"\n{user_degrees} °F es equivalente a {celsius} °C.\n")

        elif user_option == 4:

            user_degrees = int(input("\nGrados Fahrenheit: "))

            kelvin = fahren_to_kelvin(user_degrees)

            print(f"\n{user_degrees} °F es equivalente a {kelvin} K.\n")

        elif user_option == 5:

            user_degrees = int(input("\nGrados Kelvin: "))

            celsius = kelvin_to_celsius(user_degrees)

            print(f"\n{user_degrees} K es equivalente a {celsius} °C.\n")

        elif user_option == 6:

            user_degrees = int(input("\nGrados Kelvin: "))

            fahren = kelvin_to_fahren(user_degrees)

            print(f"\n{user_degrees} K es equivalente a {fahren} °F.\n")

        else:

            print("\nInserta una opción válida.\n")
    

if __name__ == "__main__":
    main()