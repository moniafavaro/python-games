# setup
yes_no = ['yes', 'no']
directions = ['felt', 'right', 'forward', 'backward']

# introduction
name = input('What is your name, adventurer?\n')
print(f'''Greetings {name},
    Let us go on a quest!
    
    You find yourself on the edge of a dark forest. You look around and there is not many routes to take.
    Can you find your way through?\n''')

# start of game
response = ''
while response not in yes_no:
    response = input('Would you like to step into the forest?\nyes/no\n')
    if response == 'yes':
        print('You head into the forest. You hear crows cawing in the distance.\n')
    elif response == 'no':
        print(f'You are not ready for this quest. Goodbye {name}.')
        quit()
    else:
        print('I did not understand that.\n')
        
# next part of game
response = ''
while response not in directions:
    print('To your felt, you see a bear.')
    print('To your right, there is more forest.')
    print('There is a rock wall directly in front of you')
    print('Behind you is the forest exit.\n')
    
    response = input('What direction do you want to move?\nleft/right/forward/backward\n')
    if response == 'left':
        print(f'The bear eats you, Farewell {name}.')
        quit()
    elif response == 'right':
        print('You head deeper into the forest.\n')
    elif response == 'forward':
        print('You cannot scale the wall.\n')
    elif response == 'backward':
        print(f'You leave the forest. Goodbye {name}.')
        quit()
    else:
        print('I did not understand that.\n')