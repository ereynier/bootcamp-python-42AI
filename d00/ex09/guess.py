import random

print("Hello this is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to \
find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck !")

while(1):
    n = random.randint(1, 99)
    find = 0
    turn = 0
    while(find == 0):
        print("What is your guess between 1 and 99 ?")
        i = input()
        try:
            i = int(i)
            turn += 1
            if (i > n):
                print("Too high!")
            elif (i < n):
                print("Too low!")
            else:
                print("Congratulation you've got it !")
                if (turn == 1):
                    print("You won in only 1 attempt you are so stong \
(or lucky)")
                else:
                    print("You won in ", turn, " attempts !")
                find = 1
        except ValueError:
            if (i == "exit"):
                print("Good bye!")
                exit()
            print("It's not a number")
    print("NEW GAME ! (type exit to leave)")
