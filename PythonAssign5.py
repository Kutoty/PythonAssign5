# You design a Program to come up with a software to convert:
#   1) Temperature from Fahrenheit to Celsius and back
#   2) Convert Nautical Miles to KMS and back,
#   3) Convert Kilometer to Miles and back,
#   4) Convert Centimeters to meters and back
#   5) Convert Yard to Meters and back,
#   6) Convert Inches to Centimeters and back
# Your program should be menu driven with Options to pick from the running program.

# Fahrenheit to Celsius and back
farToDeg = lambda x: (x - 32) * (5 / 9)
degToFar = lambda x: (x * (9 / 5)) + 32

# Nautical Miles to KMS and back
milToKm = lambda x: x * 1.609344
kmToMil = lambda x: x / 1.609344

# Centimeters to meters and back
cmToM = lambda x: x * 100
mTocm = lambda x: x / 100

# Yard to Inch and back
yardToIn = lambda x: x * 36
inToyard = lambda x: x / 36

# Inches to Centimeters and back
inToCm = lambda x: x * 2.54
cmToIn = lambda x: x / 2.54

print("Conversion Assignment by KISIO FRANCIS")
selection = "Select one of the following" \
            "\n[P]\t\tPrint Options" \
            "\n[C]\t\tConvert from Celsius" \
            "\n[F]\t\tConvert from Fahrenheit" \
            "\n[M]\t\tConvert from Miles" \
            "\n[KM]\tConvert from Kilometers" \
            "\n[CM]\tConvert from Centimeters" \
            "\n[Y]\t\tConvert from Yards" \
            "\n[IN]\tConvert from Inches" \
            "\n[Q]\t\tQuit\n"


def mySelection():
    exit = False

    while exit != True:
        conversion = input(selection)

        # execute according to solution selected
        # Reprint Options
        if conversion == "P" or conversion == "p":
            continue

        # convert degrees celsius to Fahrenheit
        elif conversion == "C" or conversion == "c":
            valToconvert = input("Enter the degrees celsius you want to convert: ")
            print("Option: C"
                  "\nTemperature in"
                  "\n\t\tdegrees celsius: " + str(valToconvert) +
                  "\n\t\tFahrenheit: " + format((degToFar(float(valToconvert))), '.2f') +
                  "\n\n")

        # convert Fahrenheit to degrees celsius
        elif conversion == "F" or conversion == "f":
            valToconvert = input("Enter the Fahrenheit value you want to convert: ")
            print("Option: F"
                  "\nTemperature in"
                  "\n\t\tFahrenheit: " + str(valToconvert) +
                  "\n\t\tdegrees celsius: " + format((farToDeg(float(valToconvert))), '.2f') +
                  "\n\n")

        # convert miles to km and meters
        elif conversion == "M" or conversion == "m":
            valToconvert = input("Enter the Miles you want to convert: ")
            print("Option: M"
                  "\nLength in"
                  "\n\t\tMiles: " + str(valToconvert) +
                  "\n\t\tKilometres: " + format((milToKm(float(valToconvert))), '.2f') +
                  "\n\t\tMetres: " + format(((milToKm(float(valToconvert))) * 1000), '.2f') +
                  "\n\n")

        # convert km to miles and metres
        elif conversion == "KM" or conversion == "km" or conversion == "Km":
            valToconvert = input("Enter the Kilometers you want to convert: ")
            print("Option: KM"
                  "\nLength in"
                  "\n\t\tKilometres: " + str(valToconvert) +
                  "\n\t\tMiles: " + format((kmToMil(float(valToconvert))), '.2f') +
                  "\n\t\tMetres: " + format((float(valToconvert) * 1000), '.2f') +
                  "\n\n")

        # convert cm to inches and metres
        elif conversion == "CM" or conversion == "cm" or conversion == "Cm":
            valToconvert = input("Enter the Centimeters you want to convert: ")
            print("Option: CM"
                  "\nLength in"
                  "\n\t\tCentimeters: " + str(valToconvert) +
                  "\n\t\tInches: " + format((cmToIn(float(valToconvert))), '.2f') +
                  "\n\t\tMetres: " + format((int(valToconvert) / 100), '.2f') +
                  "\n\n")

        # convert yards to inches and metres
        elif conversion == "Y" or conversion == "y":
            valToconvert = input("Enter the Yards you want to convert: ")
            print("Option: Y"
                  "\nLength in"
                  "\n\t\tYards: " + str(valToconvert) +
                  "\n\t\tInches: " + format((yardToIn(float(valToconvert))), '.2f') +
                  "\n\t\tMeters: " + format(((inToCm(yardToIn(float(valToconvert)))) * 100), '.2f') +
                  "\n\n")

        # convert inches to cm
        elif conversion == "IN" or conversion == "in" or conversion == "In":
            valToconvert = input("Enter the Inches you want to convert: ")
            print("Option: Y"
                  "\nLength in"
                  "\n\t\tInches: " + str(valToconvert) +
                  "\n\t\t\tCentimeters: " + format((inToCm(float(valToconvert))), '.2f') +
                  "\n\n")

        elif conversion == "Q" or conversion == "q":
            print("\nOption: Q"
                  "\nQuit")
            break
        else:
            print("Invalid Selection"
                  "\nSelect one of the options provided below e.g. C, KM or IN")


mySelection()