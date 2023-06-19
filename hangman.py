def hangman(word):
    wrong = 0
    stages = ["",
              "________  ",
              "|      |  ",
              "|      |  ",
              "|      O  ",
              "|     /|\ ",
              "|     / \ ",
              "|         "
              ]
    letters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        
        if char in letters:
            cind = letters.index(char)
            board[cind] = char
            letters[cind] = '$'
        else:
            wrong += 1
        
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        
        if "_" not in board:
            print("\nYou WIN!!!")
            print(" ".join(board))
            win = True
            break
            
    if not win:
        print("\n".join(stages[0:wrong]))
        print(f"You lose! It was {word}.")
        
hangman("penguin")