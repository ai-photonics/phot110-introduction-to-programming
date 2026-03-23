
while True:
    try:
        file_name = input("Give a valid file name: ")
        # Try to open the text-file
        with open(file_name, "r+", encoding="utf-8") as f:
            # Read the text-data
            my_text = f.read()
            # Print the text-data
            print(my_text)
        break
    except OSError as e:
        print(f"Invalid file: Please try again")
    except Exception:
        print(f"Invalid file: Please try again")
