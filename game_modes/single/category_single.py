from players import SinglePlayer
from utils.difficulty_level import set_difficulty_level
from random import choice
from word_collection import *

def play_category_single_mode():
    CS_player = SinglePlayer()
    load_request = input('A- NEW GAME \nB- LOAD GAME')
    if load_request.upper() == 'B':
        try:
            CS_player.load_game('category')
            print('SAVED STATE LOADED')
            game_state_loaded = True
            print(CS_player)
        except FileNotFoundError as f:
            print('SAVED STATE FILE NOT FOUND')
            game_state_loaded = False
            set_difficulty_level(CS_player)
            CS_player.revival_coins, CS_player.streak, CS_player.wins, CS_player.losses, CS_player.game_rounds, CS_player.coins = 20, 0, 0, 0, 1, 0
            CS_player.save_game('category')
    elif load_request.upper() == 'A':
        game_state_loaded = False
        try:
            with open('CSP_game_state.txt','w'):
                pass
        except FileNotFoundError:
            pass
        set_difficulty_level(CS_player)
        CS_player.revival_coins, CS_player.streak, CS_player.wins, CS_player.losses, CS_player.game_rounds, CS_player.coins = 20, 0, 0, 0, 1, 0
        CS_player.save_game('category')


    def get_hint():
        help = choice(word_list)
        while help in CS_player.gap_str:
            help = choice(word_list)
        for letter in word_list:
            index = ([pos for pos, letter in enumerate(word_list) if letter == help])
            for element in index:
                CS_player.word_gap[element] = help


    def end_game():
        print('GAME OVER!')
        score = ('SCORE:  %d / %d' % (CS_player.wins, CS_player.game_rounds))
        print(score)


    Description_Dict = {'A1': ['Adjective', Adjective], 'A2': ['Adverb', Adverb],
                        'B1': ['Beach', Beach],
                        'B2': ['Body', Body],
                        'C1': ['Calendar_Time', Calendar_Time], 'C2': ['Colour', Colour],
                        'C3': ['Country_City', Country_City],
                        'F1': ['Family', Family], 'F2': ['Flower', Flower],
                        'F3': ['Food_Fruit', Food_Fruit],
                        'M': ['Music', Music],
                        'N': ['Noun', Noun], 'P': ['Profession', Profession],
                        'S1': ['School', School],
                        'S2': ['Sport', Sport], 'V': ['Verb', Verb]}
    for keys, values in Description_Dict.items():
        print(keys, '=', values[0])
    if game_state_loaded is False:
        CS_player.category_selection = input(
            "Please enter the corresponding value of the words category you'd like to play: ").upper()
    else:
        pass
    Quit = False
    while not Quit:
        for keys, values in Description_Dict.items():
            if CS_player.category_selection in keys:
                word_description = values[0]
                if game_state_loaded is False:
                    CS_player.game_word = choice(values[1]).upper()
                else:
                    pass
                if game_state_loaded is False:
                    word_list = list(CS_player.game_word)
                else:
                    pass
                if game_state_loaded is False:
                    CS_player.word_gap = ('_' * len(CS_player.game_word))
                else:
                    pass
                if game_state_loaded is False:
                    CS_player.gap_str = '   '.join(CS_player.word_gap)
                else:
                    pass
                if game_state_loaded is False:
                    CS_player.word_gap = list(CS_player.word_gap)
                else:
                    pass
                if game_state_loaded is False:
                    CS_player.tries = 0
                else:
                    pass
                if game_state_loaded is False:
                    CS_player.save_game('category')
                else:
                    pass
        print('ROUND %d>>>' % CS_player.game_rounds)
        while CS_player.tries < CS_player.game_max_trial:
            CS_player.save_game('category')
            print('WORD DESCRIPTION:  ', word_description)
            print(CS_player.gap_str)
            print()
            CS_player.save_game('category')
            hint = input("GET HINT? \nENTER 'Y' OR 'y' TO CONFIRM OTHERWISE, PRESS ANY KEY:   ")
            if hint == 'y' or hint == 'Y':
                if CS_player.coins >= 10:
                    get_hint()
                    CS_player.gap_str = '   '.join(CS_player.word_gap)
                    CS_player.coins -= 10
                    print('COINS LEFT:  ', CS_player.coins)
                    CS_player.save_game('category')

                    if '_' not in CS_player.gap_str:
                        print(CS_player.gap_str)
                        win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                        'ASTONISHING!',
                                        'EYE-WATERING!',
                                        'FANTASTIC!', 'WOW!', 'OUTSTANDING!', 'OUTRAGEOUS!',
                                        'EXTRAORDINARY!',
                                        'WHOA!',
                                        'CONGRATULATIONS!']
                        print(choice(win_comment))
                        CS_player.wins += 1
                        print('WINS:  ', CS_player.wins)
                        CS_player.streak += 1
                        print('STREAK: ', CS_player.streak)
                        CS_player.save_game('category')
                        if CS_player.streak % 5 == 0:
                            streak_comment = ['%d IN A ROW!' % CS_player.streak,
                                                '%d IN %d!' % (
                                                    CS_player.streak, CS_player.streak),
                                                'CONSECUTIVE %d WINS!' % CS_player.streak,
                                                '%d AT ONCE!' % CS_player.streak]
                            print(choice(streak_comment))
                            CS_player.coins += 5
                            print('YOU EARNED 5 COINS!\t COINS:  ', CS_player.coins)
                        else:
                            CS_player.coins += 1
                            print('YOU EARNED A COIN!\t COINS:  ', CS_player.coins)

                        CS_player.save_game('category')
                        Exit = input(
                            'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                        if Exit == '1':
                            end_game()
                            Quit = True
                            game_state_loaded = False
                            CS_player.save_game('category')
                            break
                        else:
                            score = ('SCORE:  %d / %d' % (
                            CS_player.wins, CS_player.game_rounds))
                            print('SCORE:  ', score)
                            CS_player.game_rounds += 1
                            CS_player.save_game('category')
                            game_state_loaded = False
                            break
                else:
                    print('INSUFFICIENT COINS!')
                    CS_player.save_game('category')
                    pass

            else:
                guess = (input('Your guess?  ')).upper()
                CS_player.save_game('category')
                if guess in CS_player.game_word:
                    index = (
                    [pos for pos, letter in enumerate(CS_player.game_word) if letter == guess])
                    for element in index:
                        CS_player.word_gap[element] = guess
                    CS_player.gap_str = '   '.join(CS_player.word_gap)
                    CS_player.save_game('category')
                    if '_' not in CS_player.gap_str:
                        print(CS_player.gap_str)
                        win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                        'ASTONISHING!',
                                        'EYE-WATERING!', 'FANTASTIC!', 'WOW!', 'OUTSTANDING!',
                                        'OUTRAGEOUS!',
                                        'EXTRAORDINARY!', 'WHOA!', 'CONGRATULATIONS!']
                        print(choice(win_comment))
                        CS_player.wins += 1
                        print('WINS:  ', CS_player.wins)
                        CS_player.streak += 1
                        print('STREAK: ', CS_player.streak)
                        CS_player.save_game('category')
                        if CS_player.streak % 5 == 0:
                            streak_comment = ['%d IN A ROW!' % CS_player.streak,
                                                '%d IN %d!' % (
                                                    CS_player.streak, CS_player.streak),
                                                'CONSECUTIVE %d CS_player.wins!' % CS_player.streak,
                                                '%d AT ONCE!' % CS_player.streak]
                            print(choice(streak_comment))
                            CS_player.coins += 5
                            print('YOU EARNED 5 COINS!\t COINS:  ', CS_player.coins)
                        else:
                            CS_player.coins += 1
                            print('YOU EARNED A COIN!\t COINS:  ', CS_player.coins)
                        print(CS_player.gap_str)
                        CS_player.save_game('category')

                        Exit = input(
                            'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                        if Exit == '1':
                            end_game()
                            Quit = True
                            game_state_loaded = False
                            CS_player.save_game('category')
                            break
                        else:
                            score = ('SCORE:  %d / %d' % (
                            CS_player.wins, CS_player.game_rounds))
                            print('SCORE:  ', score)
                            CS_player.game_rounds += 1
                            game_state_loaded = False
                            CS_player.save_game('category')
                            break

                else:
                    CS_player.tries += 1
                    print(guess, 'is not in the word')
                    CS_player.save_game('category')

        else:
            print('MAN HANGED!!!')
            print(
                'You\'re out of tries \nGAME OVER! \nThe word is \'%s\'' % CS_player.game_word)
            revival = input(
                "REVIVE MAN? \nEnter 'y' or 'Y' to confirm otherwise, press any key:  ")
            CS_player.save_game('category')
            if revival in ['y', 'Y']:
                if CS_player.coins >= CS_player.revival_coins:
                    print('MAN REVIVED!!!')
                    CS_player.tries -= CS_player.game_max_trial
                    CS_player.coins -= CS_player.revival_coins
                    print('REMAINING COINS:  ', CS_player.coins)
                    CS_player.save_game('category')
                    continue
                else:
                    print('INSUFFICIENT COINS!')
                    CS_player.losses += 1
                    CS_player.save_game('category')
                    if CS_player.streak > 0:
                        CS_player.streak = 0
                        print('STREAK ENDS!')
                        print('LOSES: ', CS_player.losses)
                        CS_player.save_game('category')

                    Exit = input(
                        'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                    if Exit == '1':
                        end_game()
                        Quit = True
                        game_state_loaded = False
                        CS_player.save_game('category')
                        break
                    else:
                        score = ('%d/%d' % (CS_player.wins, CS_player.game_rounds))
                        print('SCORE:  ', score)
                        CS_player.game_rounds += 1
                        game_state_loaded = False
                        CS_player.save_game('category')
                        continue


            else:
                CS_player.losses += 1
                CS_player.save_game('category')
                if CS_player.streak > 0:
                    CS_player.streak = 0
                    print('STREAK ENDS!')
                    print('LOSSES: ', CS_player.losses)
                    CS_player.save_game('category')

                Exit = input(
                    'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                if Exit == '1':
                    end_game()
                    Quit = True
                    game_state_loaded = False
                    CS_player.save_game('category')
                    break
                else:
                    score = ('%d/%d' % (CS_player.wins, CS_player.game_rounds))
                    print('SCORE:  ', score)
                    CS_player.game_rounds += 1
                    game_state_loaded = False
                    CS_player.save_game('category')
        