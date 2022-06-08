from players import SinglePlayer
from utils.difficulty_level import set_difficulty_level
from random import choice
from word_collection import *

def play_random_single_mode():
    RS_player = SinglePlayer()
    load_request = input('A- NEW GAME \nB- LOAD GAME')
    if load_request.upper() == 'B':
        try:
            RS_player.load_game('random')
            print('SAVED STATE LOADED')
            game_state_loaded = True
            print(RS_player)
        except FileNotFoundError as f:
            print('SAVED STATE FILE NOT FOUND')
            game_state_loaded = False
            set_difficulty_level(RS_player)
            RS_player.revival_coins, RS_player.streak, RS_player.wins, RS_player.losses, RS_player.game_rounds, RS_player.coins = 20, 0, 0, 0, 1, 0
            RS_player.save_game('random')
    elif load_request.upper() == 'A':
        game_state_loaded = False
        try:
            with open('RSP_game_state.txt', 'w'):
                pass
        except:
            pass
        set_difficulty_level(RS_player)
        RS_player.revival_coins, RS_player.streak, RS_player.wins, RS_player.losses, RS_player.game_rounds, RS_player.coins = 20, 0, 0, 0, 1, 0
        RS_player.save_game('random')


    def get_hint():
        help = choice(word_list)
        while help in RS_player.gap_str:
            help = choice(word_list)
        for letter in word_list:
            index = ([pos for pos, letter in enumerate(word_list) if letter == help])
            for element in index:
                RS_player.word_gap[element] = help


    def end_game():
        print('GAME OVER!')
        score = ('SCORE:  %d / %d' % (RS_player.wins, RS_player.game_rounds))
        print(score)


    Quit = False
    while True:
        # GO AND REMOVE THE FOREVER WHILE LOOP USING YOUR LAPTOP
        while not Quit:
            if game_state_loaded is False:
                RS_player.game_word = choice(Word_collection).upper()
            else:
                pass
            # RS_player.game_word= 'DAISY'
            Description_Dict = {'NOUN': Noun, 'VERB': Verb, 'ADJECTIVE': Adjective,
                                'ADVERB': Adverb,
                                'SPORT': Sport,
                                'FOOD/FRUIT': Food_Fruit, 'COUNNTRY/CITY': Country_City,
                                'SCHOOL': School,
                                'BODY': Body,
                                'CALENDER/TIME': Calendar_Time,
                                'PROFESSION': Profession, 'MUSIC': Music, 'BEACH': Beach,
                                'FAMILY': Family,
                                'FLOWER': Flower, 'COLOUR': Colour}
            if game_state_loaded is False:
                word_list = list(RS_player.game_word)
            else:
                pass
            if game_state_loaded is False:
                RS_player.word_gap = ('_' * len(RS_player.game_word))
            else:
                pass
            if game_state_loaded is False:
                RS_player.gap_str = '   '.join(RS_player.word_gap)
            else:
                pass
            if game_state_loaded is False:
                RS_player.word_gap = list(RS_player.word_gap)
            else:
                pass
            if game_state_loaded is False:
                RS_player.tries = 0
            else:
                pass
            if game_state_loaded is False:
                RS_player.save_game('random')
            else:
                pass

            print('ROUND %d>>>' % RS_player.game_rounds)
            while RS_player.tries < RS_player.game_max_trial:
                RS_player.save_game('random')


                def obt_key(val):
                    for key, value in Description_Dict.items():
                        if val == value:
                            return key


                for item in Description_Dict.values():
                    if RS_player.game_word.lower() in item or RS_player.game_word.capitalize() in item:
                        print('WORD DESCRIPTION:  ', obt_key(item))
                print(RS_player.gap_str)
                print()
                RS_player.save_game('random')

                hint = input(
                    "GET HINT? \nENTER 'Y' OR 'y' TO CONFIRM OTHERWISE, PRESS ANY KEY:   ")
                if hint == 'y' or hint == 'Y':
                    if RS_player.coins >= 10:
                        get_hint()
                        RS_player.gap_str = '   '.join(RS_player.word_gap)
                        RS_player.coins -= 10
                        print('COINS LEFT:  ', RS_player.coins)
                        RS_player.save_game('random')

                        if '_' not in RS_player.gap_str:
                            print(RS_player.gap_str)
                            win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                            'ASTONISHING!',
                                            'EYE-WATERING!',
                                            'FANTASTIC!', 'WOW!', 'OUTSTANDING!', 'OUTRAGEOUS!',
                                            'EXTRAORDINARY!',
                                            'WHOA!',
                                            'CONGRATULATIONS!']
                            print(choice(win_comment))
                            RS_player.wins += 1
                            print('WINS:  ', RS_player.wins)
                            RS_player.streak += 1
                            print('STREAK: ', RS_player.streak)
                            RS_player.save_game('random')
                            if RS_player.streak % 5 == 0:
                                streak_comment = ['%d IN A ROW!' % RS_player.streak,
                                                    '%d IN %d!' % (
                                                        RS_player.streak, RS_player.streak),
                                                    'CONSECUTIVE %d WINS!' % RS_player.streak,
                                                    '%d AT ONCE!' % RS_player.streak]
                                print(choice(streak_comment))
                                RS_player.coins += 5
                                print('YOU EARNED 5 COINS!\t COINS:  ', RS_player.coins)
                            else:
                                RS_player.coins += 1
                                print('YOU EARNED A COIN!\t COINS:  ', RS_player.coins)
                            RS_player.save_game('random')
                            Exit = input(
                                'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                            if Exit == '1':
                                end_game()
                                Quit = True
                                game_state_loaded = False
                                RS_player.save_game('random')
                                break
                            else:
                                score = ('SCORE:  %d / %d' % (
                                    RS_player.wins, RS_player.game_rounds))
                                print('SCORE:  ', score)
                                RS_player.game_rounds += 1
                                game_state_loaded = False
                                RS_player.save_game('random')
                                break
                    else:
                        print('INSUFFICIENT COINS!')
                        RS_player.save_game('random')
                        pass

                else:
                    guess = (input('Your guess?  ')).upper()
                    RS_player.save_game('random')
                    if guess in RS_player.game_word:
                        index = ([pos for pos, letter in enumerate(RS_player.game_word) if
                                    letter == guess])
                        for element in index:
                            RS_player.word_gap[element] = guess
                        RS_player.gap_str = '   '.join(RS_player.word_gap)
                        RS_player.save_game('random')
                        if '_' not in RS_player.gap_str:
                            print(RS_player.gap_str)
                            win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                            'ASTONISHING!',
                                            'EYE-WATERING!', 'FANTASTIC!', 'WOW!',
                                            'OUTSTANDING!', 'OUTRAGEOUS!',
                                            'EXTRAORDINARY!', 'WHOA!', 'CONGRATULATIONS!']
                            print(choice(win_comment))
                            RS_player.wins += 1
                            print('WINS:  ', RS_player.wins)
                            RS_player.streak += 1
                            print('STREAK: ', RS_player.streak)
                            RS_player.save_game('random')
                            if RS_player.streak % 5 == 0:
                                streak_comment = ['%d IN A ROW!' % RS_player.streak,
                                                    '%d IN %d!' % (
                                                        RS_player.streak, RS_player.streak),
                                                    'CONSECUTIVE %d WINS!' % RS_player.streak,
                                                    '%d AT ONCE!' % RS_player.streak]
                                print(choice(streak_comment))
                                RS_player.coins += 5
                                print('YOU EARNED 5 COINS!\t COINS:  ', RS_player.coins)
                            else:
                                RS_player.coins += 1
                                print('YOU EARNED A COIN!\t COINS:  ', RS_player.coins)
                            print(RS_player.gap_str)
                            RS_player.save_game('random')

                            Exit = input(
                                'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                            if Exit == '1':
                                end_game()
                                Quit = True
                                game_state_loaded = False
                                RS_player.save_game('random')
                                break
                            else:
                                score = ('SCORE:  %d / %d' % (
                                    RS_player.wins, RS_player.game_rounds))
                                print('SCORE:  ', score)
                                RS_player.game_rounds += 1
                                game_state_loaded = False
                                RS_player.save_game('random')
                                break

                    else:
                        RS_player.tries += 1
                        print(guess, 'is not in the word')
                        RS_player.save_game('random')

            else:
                print('MAN HANGED!!!')
                print(
                    'You\'re out of tries \nGAME OVER! \nThe word is \'%s\'' % RS_player.game_word)
                revival = input(
                    "REVIVE MAN? \nEnter 'y' or 'Y' to confirm otherwise, press any key:  ")
                RS_player.save_game('random')
                if revival in ['y', 'Y']:
                    if RS_player.coins >= RS_player.revival_coins:
                        print('MAN REVIVED!!!')
                        RS_player.tries -= RS_player.game_max_trial
                        RS_player.coins -= RS_player.revival_coins
                        RS_player.revival_coins += 10
                        print('REMAINING COINS:  ', RS_player.coins)
                        RS_player.save_game('random')
                        continue
                    else:
                        print('INSUFFICIENT COINS!')
                        RS_player.losses += 1
                        RS_player.save_game('random')
                        if RS_player.streak > 0:
                            RS_player.streak = 0
                            print('STREAK ENDS!')
                            print('LOSES: ', RS_player.losses)
                            RS_player.save_game('random')
                        Exit = input(
                            'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                        if Exit == '1':
                            end_game()
                            Quit = True
                            game_state_loaded = False
                            RS_player.save_game('random')
                            break
                        else:
                            score = ('%d/%d' % (RS_player.wins, RS_player.game_rounds))
                            print('SCORE:  ', score)
                            RS_player.game_rounds += 1
                            game_state_loaded = False
                            RS_player.save_game('random')
                            continue


                else:
                    RS_player.losses += 1
                    RS_player.save_game('random')
                    if RS_player.streak > 0:
                        RS_player.streak = 0
                        print('STREAK ENDS!')
                        print('LOSES: ', RS_player.losses)
                        RS_player.save_game('random')

                    Exit = input(
                        'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                    if Exit == '1':
                        end_game()
                        Quit = True
                        game_state_loaded = False
                        RS_player.save_game('random')
                        break
                    else:
                        score = ('%d/%d' % (RS_player.wins, RS_player.game_rounds))
                        print('SCORE:  ', score)
                        RS_player.game_rounds += 1
                        game_state_loaded = False
                        RS_player.save_game('random')