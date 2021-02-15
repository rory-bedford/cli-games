# Import statements:
import time

def game():
    # Setting up a 2 dimensional dictionary containing the values of each entry:

    dict = {1: {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' '},
            2: {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' '},
            3: {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' '},
            4: {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' '},
            5: {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' '},
            6: {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' '}}

    # Setting up main string which is formatted by the dictionary:

    main_string = '  1   2   3   4   5   6   7\n --- --- --- --- --- --- ---\n| {dict[1][1]} | {dict[1][2]} | {dict[1][3]} | {dict[1][4]} | {dict[1][5]} | {dict[1][6]} | {dict[1][7]} |\n -- -- --- --- --- --- ---\n| {dict[2][1]} | {dict[2][2]} | {dict[2][3]} | {dict[2][4]} | {dict[2][5]} | {dict[2][6]} | {dict[2][7]} |\n --- --- --- --- --- --- ---\n| {dict[3][1]} | {dict[3][2]} | {dict[3][3]} | {dict[3][4]} | {dict[3][5]} | {dict[3][6]} | {dict[3][7]} |\n --- --- --- --- --- --- ---\n| {dict[4][1]} | {dict[4][2]} | {dict[4][3]} | {dict[4][4]} | {dict[4][5]} | {dict[4][6]} | {dict[4][7]} |\n --- --- --- --- --- --- ---\n| {dict[5][1]} | {dict[5][2]} | {dict[5][3]} | {dict[5][4]} | {dict[5][5]} | {dict[5][6]} | {dict[5][7]} |\n --- --- --- --- --- --- ---\n| {dict[6][1]} | {dict[6][2]} | {dict[6][3]} | {dict[6][4]} | {dict[6][5]} | {dict[6][6]} | {dict[6][7]} |\n --- --- --- --- --- --- ---'

    # Introductory print statements:
    print('\nThanks for choosing to play four in a row!\n')
    print('The format is as follows:\n')
    print('Crosses goes first, selecting a number from 1 to 7, which represents the column they want to place their coin in, as shown:\n')
    print(main_string.format(dict=dict))
    print('Then noughts enters a number, and so on.\n')
    print('The game ends when someone has 4 in a row, or when all squares are filled, resulting in a draw.\n')
    print('If you want, you can then play again, with noughts going first this time.\n')
    print('We will tally up how many games each player wins to declare an overall winner once you decide to end!\n')

    # Set up list of valid moves:

    list_valid = [1, 2, 3, 4, 5, 6, 7]

    # Set up play again variable:

    play_again = True

    # Set up dictionary of names:

    names = {'X':'Crosses', 'O':'Noughts'}

    # Set up dictionary with tallied scores:

    scores = {'Crosses':0, 'Noughts':0}

    # Number of games variable:

    number_games = 0

    # Number of goes in this game variable:

    number_goes = 0

    # While loop containing iterations of different games:

    while play_again == True:

        # Reinitialise dictionary:

        dict = {1: {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' '},
                2: {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' '},
                3: {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' '},
                4: {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' '},
                5: {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' '},
                6: {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' '}}

        # Adding 1 to number goes so noughts and crosses alternate each game:

        number_goes += number_games

        # Check if game is over:

        game_over = False

        # Main while loop with the whole game:

        while game_over == False:

            # Assign which player's go it is:
            if number_goes % 2 == 0:
                character = 'X'
            else:
                character = 'O'

            # Character's go:
            # Ask user for move, checking that it is a valid move:

            print('{} enter your move:'.format(character))

            valid_move = False

            while valid_move == False:
                move = int(input())

                # Check move is valid:
                if move not in list_valid:
                    print('Invalid move! Please try again:')
                elif dict[1][move] != ' ':
                    print('Invalid move! Please try again:')
                else:
                    valid_move = True

            # We now animate the character falling into position:

            row_pos = 1
            loop_continue = True

            while loop_continue == True:
                try:
                    dict[row_pos - 1][move] = ' '
                except Exception:
                    pass
                dict[row_pos][move] = character
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                print(main_string.format(dict=dict)+'\n')
                try:
                    if dict[row_pos + 1][move] != ' ':
                        loop_continue = False
                except Exception:
                    loop_continue = False
                row_pos += 1
                time.sleep(0.6)

            row_pos += -1
            number_goes += 1

            # Check if character has won the game:
            # One verticle condition:
            try:
                if dict[row_pos + 3][move] == character and dict[row_pos + 2][move] == character and dict[row_pos + 1][move] == character:
                    game_over = True
            except Exception:
                pass

            # Four horizontal conditions:
            try:
                if dict[row_pos][move + 3] == character and dict[row_pos][move + 2] == character and dict[row_pos][move + 1] == character:
                    game_over = True
            except Exception:
                pass

            try:
                if dict[row_pos][move + 2] == character and dict[row_pos][move + 1] == character and dict[row_pos][move - 1] == character:
                    game_over = True
            except Exception:
                pass

            try:
                if dict[row_pos][move + 1] == character and dict[row_pos][move - 1] == character and dict[row_pos][move - 2] == character:
                    game_over = True
            except Exception:
                pass

            try:
                if dict[row_pos][move - 1] == character and dict[row_pos][move - 2] == character and dict[row_pos][move - 3] == character:
                    game_over = True
            except Exception:
                pass

            # Four positive grad diagonal conditions:
            try:
                if dict[row_pos - 1][move + 1] == character and dict[row_pos - 2][move + 2] == character and dict[row_pos - 3][move + 3] == character:
                    game_over = True
            except Exception:
                pass

            try:
                if dict[row_pos + 1][move - 1] == character and dict[row_pos - 1][move + 1] == character and dict[row_pos - 2][move + 2] == character:
                    game_over = True
            except Exception:
                pass
            try:
                if dict[row_pos + 2][move - 2] == character and dict[row_pos - 1][move + 1] == character and dict[row_pos + 1][move - 1] == character:
                    game_over = True
            except Exception:
                pass

            try:
                if dict[row_pos + 3][move - 3] == character and dict[row_pos + 2][move - 2] == character and dict[row_pos + 1][move - 1] == character:
                    game_over = True
            except Exception:
                pass

            # Four negative grad diagonal conditions:
            try:
                if dict[row_pos + 1][move + 1] == character and dict[row_pos + 2][move + 2] == character and dict[row_pos + 3][move + 3] == character:
                    game_over = True
            except Exception:
                pass

            try:
                if dict[row_pos - 1][move - 1] == character and dict[row_pos + 1][move + 1] == character and dict[row_pos + 2][move + 2] == character:
                    game_over = True
            except Exception:
                pass

            try:
                if dict[row_pos - 2][move - 2] == character and dict[row_pos - 1][move - 1] == character and dict[row_pos + 1][move + 1] == character:
                    game_over = True
            except Exception:
                pass

            try:
                if dict[row_pos - 3][move - 3] == character and dict[row_pos - 2][move - 2] == character and dict[row_pos - 1][move - 1] == character:
                    game_over = True
            except Exception:
                pass

        # Print congrats message
        winner = names[character]
        print('{} wins! Congratulations!\n'.format(winner))

        # Add tally to total scores:
        scores[names[character]] += 1

        # Print total scores so far:
        print(f'Scores so far:\n\nCrosses: {scores["Crosses"]}\nNoughts: {scores["Noughts"]}\n')

        # Ask if they would like to play again:

        print('Would you like to play again? (y/n)\n')

        answer = input()

        if answer == 'n':
            play_again = False

    print(f'Thanks for playing! The final scores are:\n\nCrosses: {scores["Crosses"]}\nNoughts: {scores["Noughts"]}\n')

    if scores['Crosses'] > scores['Noughts']:
        print('Crosses is the overall winner! Congratulations!')
    elif scores['Crosses'] == scores['Noughts']:
        print('''Overall it's a draw, well done both of you!''')
    else:
        print('Noughts is the overall winner! Congratulations!')
