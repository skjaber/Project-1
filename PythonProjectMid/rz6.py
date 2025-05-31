import random
num_guess = random.randint(1,100)
attempts = 5
print("Guess number between 1 to 100 , you have 5 attempt")

while attempts > 0:
    guess = int(input("enter your guess: "))
    if guess == num_guess:
        print("U r r8")
        break
    elif guess < num_guess:
        print("Too low")
    else:
        print("too high")
    attempts -= 1

if attempts == 0:
    print(f"sorry, u r end of attempts. number is {num_guess}.")
