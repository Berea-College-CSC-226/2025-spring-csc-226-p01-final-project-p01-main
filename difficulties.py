def get_difficulty():
    print("Choose difficulty: Normal, or Hard")

    while True:
        choice = input("Enter difficulty: ").lower()
        if choice == "normal":
            return 1.0  # Normal turtle speed
        elif choice == "hard":
            return 0.5
        else:
            print("Invalid choice. Please enter, Normal, or Hard.")
