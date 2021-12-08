import random
import time


class color:
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    RED     = '\033[31m'
    WHITE   = '\033[37m'

run = True
choices = ["f", "w", "g"]

print("Explanation: Fire -> Ground -> Water -> Fire")
answer = input(color.GREEN + "Welcome to the game 'Fire - Water - Ground !'\nReady? Y or N: ").lower()


while True:

    if answer == "n" :
        run = False
        print(color.RED + "I known you were scared.. See you later")
        break
    elif answer == "y" :
        print(color.GREEN + "We play 10 round, let the better one win!\n Let's start")
        break
    else:
        answer = (input("Choose beetwen Y or N..:").lower())
        
    
i = 0
score = 0
computer_score=0

while run and i < 10:

    comp_choice = random.choice(choices)
    user_choice = input(color.WHITE + "Type f for fire, w for water or g for ground: ").lower()

    if user_choice == comp_choice:
        print(color.YELLOW + "Game draws.Play again" )
        
    elif user_choice == "f" and comp_choice == "w":
        print(color.RED + "It's Fire vs Water You lose!" )
        computer_score += 1

    elif user_choice == "f" and comp_choice == "g":
        print(color.GREEN + "It's Fire vs Ground. You won" )
        score += 1 

    elif user_choice == "w" and comp_choice == "f":
        print(color.GREEN + "It's Water vs Fire You Win!" )
        score +=1

    elif user_choice == "w" and comp_choice == "g":
        print(color.RED + "It's Water vs Ground. You lose" )
        computer_score += 1

    elif user_choice == "g" and comp_choice == "w":
        print(color.GREEN + "It's Ground vs Water You win!" )
        score +=1

    elif user_choice == "g" and comp_choice == "f":
        print(color.RED + "It's Ground vs Fire. You lose" )
        computer_score += 1

    else:
        print("Wrong input")
        continue
    
    i += 1
    print(f"{10-i} matches left")

if run == True:
    print(f"Your score is {score} and the final result is...")
    time.sleep(2)
    if score > computer_score:
        print(color.GREEN + "You won...Next time i'll beat You!!" )
    elif score == computer_score:
        print(color.YELLOW + "Its a draw..")
    elif score < computer_score:
        print(color.RED + "Easy game, You lose!" +  "Better luck next time\n See You soon!" )