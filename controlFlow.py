def game():
    print("You've entered the game!")
    print("Please enter 'a' or 'b'")
    answer = raw_input("Type 'a' or 'b' and hit 'Enter' ").lower()
    if answer == "a" :
        print("You entered 'a'.Bye")
    elif answer == "b" :
        print("You entered 'b'.Bye")
    else :
        print("You need to enter a letter which in 'a' or 'b' to exit.")
        game()

game()
