import random

number = random.randint(1,10)

player_name = input('Hello player, what is your name? ')
number_of_guesses = 0
print(f'Okay {player_name}, guess a number between 1 and 10: ')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    
    if guess < number:
        print('Your guess is too low')
    elif guess > number:
        print('Your guess is too high')
    elif guess == number:
        break
    
if guess == number:
    print(f'You guessed the number in {str(number_of_guesses)} tries!!')
else:
    print(f'You did not guess the number. The right number was {str(number)}')