import random

print("Enter the range of numbers (From-To) : ", end="")
lowerNum = int(input())
higherNum = int(input())

with open(f"highScore_{lowerNum}_to_{higherNum}.txt", "a") as file:
    pass

with open(f"highScore_{lowerNum}_to_{higherNum}.txt") as file:
    highScore = file.read()
    if(highScore == ""):
        highScore = 0
    else:
        highScore = int(highScore)

if(highScore == 0):
    print(f"There is no current high score for {lowerNum}-{higherNum}.") 
else:
    print(f"The current lowest number of guesses for {lowerNum}-{higherNum} are : {highScore}")

print("Let's see if you can beat this😘")
print("===============================")

random_Number = random.randint(lowerNum,higherNum)
number_of_attempts = 0

while(True):
    number_of_attempts += 1
    if(number_of_attempts == 1):
        guessed_number = int(input(f"Guess a number between {lowerNum} to {higherNum} : "))
    else:
        guessed_number = int(input("Guess : "))

    if(guessed_number > random_Number):
        print("A lil lower please. Try Again.")

    elif(guessed_number < random_Number):
        print("A lil higher please. Try Again.")

    elif(guessed_number == random_Number):
        print("===============================")
        print("Oh yeah!! You guessed it right.")
        break

print(f"Total Attempts : {number_of_attempts}")

if(highScore == 0 or number_of_attempts < highScore):
    print("That's a new high score. Congrats!")
    with open(f"highScore_{lowerNum}_to_{higherNum}.txt","w") as file:
        file.write(str(number_of_attempts))
else:
    print("Couldn't beat the high score this time. Better luck next time.")

resetHighScore = input("Press Y to reset High-Score, else to exit : ")
if(resetHighScore.lower() == "y"):
    with open(f"highScore_{lowerNum}_to_{higherNum}.txt","w") as file:
        file.write(str(0))
    print("HIGH SCORE RESETED.")
else:
    print("Byee👋")
