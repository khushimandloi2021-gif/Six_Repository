### creat  a rock,paper,scissor,game
### play with computer (where computer choose randomely,not conditionaly)
### get the input from user and print the result

import random  


game_console ='''    
 _____________________________   
/        _____________        \  
| == .  |             |     o |  
|   _   |             |    B  |  
|  / \  |             | A   O |  
| | O | |             |  O    |  
|  \_/  |             |       |  
|       |             | . . . |  
|  :::  |             | . . . |  
|  :::  |_____________| . . . |  
|           S N K             |  
\_____________________________/
'''
print(game_console)
user_choice = input("enter your choice (rock,paper,scissor): ")
computer_choice = random.choice(["rock","scissor","paper"])

print(user_choice, computer_choice )

if user_choice == computer_choice:
    print("match tie")
elif user_choice == "rock" :
    if computer_choice == "paper":
       print("computer win,paper covers rock")
    else:
       print("rock smashes scissor,you won")
elif user_choice == "paper" :
    if computer_choice == "rock":
     print("user win,paper covers rock")
    else:
     print("scissor win,sciccor cut the paper")
elif user_choice == "scissor":
    if computer_choice == "rock":
       print("computer win,rock crushes scissor")
    else:
       print("scissor win ,scissor cut paper")



