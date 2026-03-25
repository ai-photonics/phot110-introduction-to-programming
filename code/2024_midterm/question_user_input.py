import math

while True:
    number_str = input("Give a decimal number in interval [0, 100]: ")
    try:
        number = float(number_str)
        if (number <= 100) and (number >= 0):
            print("The number you provided has:")
            print(f"\tinteger part: {math.floor(number)}")
            print(f"\tdecimal part: {number - math.floor(number)}")
            if number < 50:
                print("The number is smaller than 50")
            else:
                print("The number is larger than or equal to 50")
            break
        else:
            print("The number " + number_str + " is out of range, please try again.")
    except ValueError:
        print("The number " + number_str + " is invalid, please try again.")
