# Introductory print statements:
print('\nThanks for choosing to play noughts and crosses!\n')
print('The format is as follows:\n')
print('Crosses goes first, selecting a number from 1 to 9, which represent positions on the board as shown below:\n')
print(' 1 | 2 | 3\n--- --- ---\n 4 | 5 | 6\n--- --- ---\n 7 | 8 | 9\n')
print('Then noughts enters a number, and so on.\n')
print('The game ends when someone has 3 in a row, or when all squares are filled, resulting in a draw.\n')

# Setting up dictionary containing all entries played up to that point:

dict = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' ',}

# Print initial blank board:

print(' {0} | {1} | {2}     1 | 2 | 3\n--- --- ---   --- --- ---\n {3} | {4} | {5}     4 | 5 | 6\n--- --- ---   --- --- ---\n {6} | {7} | {8}     7 | 8 | 9'.format(dict['1'],dict['2'],dict['3'],dict['4'],dict['5'],dict['6'],dict['7'],dict['8'],dict['9']))

# Setting up game finished variable:

game_over = False

# Variable which checks if it's X's or O's go:

number_moves = 0

# Defining the exit message for who wins:

exit_message = 'Congratulations {}, you won!'

# While loop containing the whole game:

while game_over is False:

    # Set valid_move variable back to false so it repeats while loop:

    valid_move = False

    # Assign player variable to whichever character's go it is, then add 1 to number_moves for next go:
    if number_moves % 2 == 0:
        player = 'X'
    else:
        player = 'O'
    number_moves += 1


    # While loop runs on the first go, or if the player enters an invalid move
    while valid_move == False:
        go = str(input('\n{} enter your move:\n\n'.format(player)))
        if dict[go] == ' ':
            valid_move = True
        else:
            valid_move = False
            print('\nYou have entered an invalid number! Please try again.\n')

    # Replace correct index with player variable and print the whole image
    dict[go] = player
    print('\n {0} | {1} | {2}     1 | 2 | 3\n--- --- ---   --- --- ---\n {3} | {4} | {5}     4 | 5 | 6\n--- --- ---   --- --- ---\n {6} | {7} | {8}     7 | 8 | 9\n'.format(dict['1'],dict['2'],dict['3'],dict['4'],dict['5'],dict['6'],dict['7'],dict['8'],dict['9']))

    # Exit strategy:

    if dict['1'] == player and dict['2'] == player and dict['3'] == player:
        game_over = True
        print(exit_message.format(player))
        exit()
    elif dict['4'] == player and dict['5'] == player and dict['6'] == player:
        game_over = True
        print(exit_message.format(player))
        exit()
    elif dict['7'] == player and dict['8'] == player and dict['9'] == player:
        game_over = True
        print(exit_message.format(player))
        exit()
    elif dict['1'] == player and dict['4'] == player and dict['7'] == player:
        game_over = True
        print(exit_message.format(player))
        exit()
    elif dict['2'] == player and dict['5'] == player and dict['8'] == player:
        game_over = True
        print(exit_message.format(player))
        exit()
    elif dict['3'] == player and dict['6'] == player and dict['9'] == player:
        game_over = True
        print(exit_message.format(player))
        exit()
    elif dict['1'] == player and dict['5'] == player and dict['9'] == player:
        game_over = True
        print(exit_message.format(player))
        exit()
    elif dict['7'] == player and dict['5'] == player and dict['3'] == player:
        game_over = True
        print(exit_message.format(player))
        exit()

    if number_moves == 9:
        game_over = True
        print('''It's a draw! Better luck next time!''')
        exit()
