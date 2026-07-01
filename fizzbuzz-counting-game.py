# fizz buzz game

number = 1

while number <= 101:
    
    # Kya yeh number FizzBuzz hai?
    if number % 3 == 0 and number % 5 == 0:
        word = "fizzBuzz"
    elif number % 3 == 0:
        word = "fizz"
    elif number % 5 == 0:
        word = "buzz"
    else:
        word = str(number)
    
    if number % 2 != 0:
        # Computer ki turn
        print("Computer:", word)
        number += 1
    else:
        # User ki turn
        user_input = input(f"Your turn: ")
        if user_input == word:
            number += 1
        else:
            print("Wrong! Try again. Hint:", word)