from random import randint

play_options = ['Rock', 'Paper', 'Scissors']

computer_player = play_options[randint(0,2)]
human_player = False

while human_player == False:
    human_player = input('Rock, Paper or Scissors? ')
    if human_player == computer_player:
        print('oh, it is a TIE!! \U0001F910')
    elif human_player == 'Rock':
        if computer_player == 'Paper':
            print('You lose!! \U0001F612', computer_player, 'covers', human_player)
        else:
            print('You win!!!! \U0001F601', human_player, 'smashes', computer_player)
    elif human_player == 'Paper':
        if computer_player == 'Scissors':
            print('You lose... \U0001F612', computer_player, 'smashes', human_player)
        else:
            print('You win!!! \U0001F601', human_player, 'cuts', computer_player)
    else:
        print('That is not a valid play. Check your spelling! \U0001F607')
        
    human_player = False
    computer_player = play_options[randint(0,2)]
