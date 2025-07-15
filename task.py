while True:
    print("Welcome to the Pattern Generator and Number Analyzer!")

    print("Select an option:")
    print("1. Right-angled Triangle")
    print("2. Pyramid")
    print("3. Left-angled Triangle")
    print("Analyze a Range of numbers")

    option = int(input{"Enter your choice(1/2/3/4):"})
    if option == "1":
        for i in range(1, 6):
            for j in range(1, i+1):
                print("*", end=" ")
            print("")
    elif option == "2":
        for a in range(1, 5+1):
            print(" " * (5 - 1), end=" ")
            print("* " * (2 * i -1))
    elif choice == "3":
        for i in range(1, 5 + 1):
            print(" " * (5 - 1), end=" ")
            print("* " * i)
    elif choice == "4":
        a_range = int(input("Enter your starting range: "))
        b_range = int(input("Enter your ending range: "))
        for i in range(a_range, b_range+1):
            total = 0
            if ((i % 2) != 0):
                print(f"Number {i} is Odd")
            elif ((i % 2) == 0):
                print(f"Number {i} is Even")
        total = (a_range + b_range)/2
        print(int(total))
    elif choice == "q":
        print("Program Dismissed!")
        break
    else:
        print("Invalid input!")
        break
    
    
