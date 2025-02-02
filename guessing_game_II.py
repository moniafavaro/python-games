import random

num = random.randrange(1000, 9999)

n = int(input('Guess the 4 digit number: '))

if (n == num):
    print('Great!!! You guessed the number in just 1 try.')
else:
    tries = 0
    while (n != num):
        tries += 1 # how many guesses were made
        count = 0
        n = str(n)
        num = str(num)
        correct = [] # for digits which are correct

        # for loop runs 4 times to give 4 digits
        for i in range(0, 4):
            if (n[i] == num[i]):
                count += 1
                correct.append(n[i])
            else:
                continue
        
        if (count < 4) and (count != 0):
            print(f'Not quite the number, but you did get {count} digit(s) correct!')
            
            print('Also these numbers in your input were correct:')
            for k in correct:
                print(k, end=' ')

            print('\n')
            print('\n')
            n = int(input('Enter your next choice of numbers: '))
        
        elif(count == 0):
            print('None of your numbers matched')
            n = int(input('Enter your next choice of numbers: '))
        
    if (n == num):
        print('You have become a Mastermind!')
        print(f'It took you only {tries} tries.')
