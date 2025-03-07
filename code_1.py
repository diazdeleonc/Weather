#Name Carlos Diaz de Leon
#CODE 1 - Weather Assistant
#Conversion formula: (Temperature in °F - 32) * .5556
#Note that the message to user should be the following "What is the temperature outside:"

def main():
    temperature = input("What is the temperature outside:")
    celcius_temperature = (float(temperature)-32) * .5556

    if celcius_temperature >= 20:
        print("\nWear a hat")
    elif celcius_temperature <20 and celcius_temperature >= 10:
        print("\nWear a light jacket")
    else:
        print("\nWear a heavy jacket")
            


if __name__ == "__main__":
    main()
