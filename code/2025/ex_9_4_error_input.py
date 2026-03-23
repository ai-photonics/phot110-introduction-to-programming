while True:
    try:
        height = float(input("\tYour height (in cm) = "))
        print(f"You are {height} cm")
        break
    except ValueError:
        print(f"Invalid input: please try again")
