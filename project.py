while True:
    name : str = input("What is your name? ")

    if name.isalpha():
        age= (input("How old are you? "))        
    
        if age.isdigit():
            print(f"{name}, You are {age} years old!")
            break

        else:
            print("Enter correct age using numbers only")
    else:
        print("Enter correct name using letters only")