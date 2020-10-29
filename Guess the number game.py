import random

play = True
def replay():                                               
    playAgain = input("Do you want to play again (y/n) ? ")
    if playAgain.lower() == 'y':
        return True
    if playAgain.lower() == 'n':    
        print(*results, sep = "\n")
        return False
results = []
order_number = 0
while play:
    n1 = int(input("Choose a number in range 1- "))
    number = random.randint(1, n1)
    guesses = 1
    print(f"guess the number in range 1-{n1}")
    while True:
        guess = input()
        guess = int(guess)
        if guess == number:
            order_number += 1
            print(f"You guessed it! \n it took you {guesses} guesses")
            results.append(f"attempt {order_number}: {guesses} guesses, range 1-{n1}")
            play = replay()
            break
        elif guess > number:
            print("The number is smaller")
            guesses += 1
        elif guess < number:
            print("The number is bigger")
            guesses += 1



