from random import choice
from word_collection import *
from utils.difficulty_level import set_difficulty_level
from players import Player

def play_career_mode():
    player = Player()
    try:
        player.load_game()
        game_state_loaded = True
        print(player)
    except FileNotFoundError as f:
        game_state_loaded = False
        print('PLEASE CREATE PLAYER PROFILE')
        player.name = input('Please enter player name:  ').upper()
        print('WELCOME TO THE HANGMAN WORLD, %s!' % player.name)
        set_difficulty_level(player)
        player.game_revival_coins = 20
        player.streak = 0
        player.game_rounds = 1
        player.wins = 0
        player.losses = 0
        player.coins = 5000
        player.save_game()


    def get_hint():
        help = choice(word_list)
        while help in player.gap_str:
            help = choice(word_list)
        for letter in word_list:
            index = ([pos for pos, letter in enumerate(word_list) if letter == help])
            for element in index:
                player.word_gap = list(player.word_gap)
                player.word_gap[element] = help


    def end_game():
        print('GAME OVER!')
        score = ('SCORE:  %d / %d' % (player.wins, player.game_rounds))
        print(score)
        GameOn = True
        ExitForLoop = True
        ExitForLoop2 = True
        Quit = True
        return


    game_Level_WordLength_dict = {1: ['UNLOCKED', [20, 14, 15, 16, 2, 4]], 2: ['LOCKED', [5, 6, 11]],
                                    3: ['LOCKED', [5, 6, 11]],
                                    4: ['LOCKED', [7, 8, 12, 13, 18, 19]],
                                    5: ['LOCKED', [7, 8, 12, 13, 18, 19]], 6: ['LOCKED', [9, 10]]}
    player.game_division_dict = {1: ['UNLOCKED', 'rating1', 'NOT PLAYED'],
                                    2: ['LOCKED', 'rating2', 'NOT PLAYED'],
                                    3: ['LOCKED', 'rating3', 'NOT PLAYED'],
                                    4: ['LOCKED', 'rating4', 'NOT PLAYED'],
                                    5: ['LOCKED', 'rating5', 'NOT PLAYED'],
                                    6: ['LOCKED', 'rating6', 'NOT PLAYED'],
                                    7: ['LOCKED', 'rating7', 'NOT PLAYED'],
                                    8: ['LOCKED', 'rating8', 'NOT PLAYED'],
                                    9: ['LOCKED', 'rating9', 'NOT PLAYED'],
                                    10: ['LOCKED', 'rating10', 'NOT PLAYED'],
                                    11: ['LOCKED', 'rating11', 'NOT PLAYED'],
                                    12: ['LOCKED', 'rating12', 'NOT PLAYED'],
                                    13: ['LOCKED', 'rating13', 'NOT PLAYED'],
                                    14: ['LOCKED', 'rating14', 'NOT PLAYED'],
                                    15: ['LOCKED', 'rating15', 'NOT PLAYED'],
                                    16: ['LOCKED', 'rating16', 'NOT PLAYED'],
                                    17: ['LOCKED', 'rating17', 'NOT PLAYED'],
                                    18: ['LOCKED', 'rating18', 'NOT PLAYED'],
                                    19: ['LOCKED', 'rating19', 'NOT PLAYED'],
                                    20: ['LOCKED', 'rating20', 'NOT PLAYED'],
                                    21: ['LOCKED', 'rating21', 'NOT PLAYED'],
                                    22: ['LOCKED', 'rating22', 'NOT PLAYED'],
                                    23: ['LOCKED', 'rating23', 'NOT PLAYED'],
                                    24: ['LOCKED', 'rating24', 'NOT PLAYED'],
                                    25: ['LOCKED', 'rating25', 'NOT PLAYED'],
                                    26: ['LOCKED', 'rating26', 'NOT PLAYED'],
                                    27: ['LOCKED', 'rating27', 'NOT PLAYED'],
                                    28: ['LOCKED', 'rating28', 'NOT PLAYED'],
                                    29: ['LOCKED', 'rating29', 'NOT PLAYED'],
                                    30: ['LOCKED', 'rating30', 'NOT PLAYED'],
                                    31: ['LOCKED', 'rating31', 'NOT PLAYED'],
                                    32: ['LOCKED', 'rating32', 'NOT PLAYED'],
                                    33: ['LOCKED', 'rating33', 'NOT PLAYED'],
                                    34: ['LOCKED', 'rating34', 'NOT PLAYED'],
                                    35: ['LOCKED', 'rating35', 'NOT PLAYED'],
                                    36: ['LOCKED', 'rating36', 'NOT PLAYED'],
                                    37: ['LOCKED', 'rating37', 'NOT PLAYED'],
                                    38: ['LOCKED', 'rating38', 'NOT PLAYED'],
                                    39: ['LOCKED', 'rating39', 'NOT PLAYED'],
                                    40: ['LOCKED', 'rating40', 'NOT PLAYED'],
                                    41: ['LOCKED', 'rating41', 'NOT PLAYED'],
                                    42: ['LOCKED', 'rating42', 'NOT PLAYED'],
                                    43: ['LOCKED', 'rating43', 'NOT PLAYED'],
                                    44: ['LOCKED', 'rating44', 'NOT PLAYED'],
                                    45: ['LOCKED', 'rating45', 'NOT PLAYED'],
                                    46: ['LOCKED', 'rating46', 'NOT PLAYED'],
                                    47: ['LOCKED', 'rating47', 'NOT PLAYED'],
                                    48: ['LOCKED', 'rating48', 'NOT PLAYED'],
                                    49: ['LOCKED', 'rating49', 'NOT PLAYED'],
                                    50: ['LOCKED', 'rating50', 'NOT PLAYED']}


    def level_security():
        if player.game_difficulty.upper() in ['A', 'B', '']:
            global stop_game
            stop_game = False
            if stop_game2 == False:
                for key, values in game_Level_WordLength_dict.items():
                    if player.game_level == key:
                        while values[0] == 'LOCKED':
                            stop_game = True
                            print('LEVEL LOCKED! \nUNLOCK PREVIOUS LEVEL FIRST')
                            return
                        else:
                            stop_game = None
                            return
            else:
                for key, values in player.game_division_dict.items():
                    if player.game_division == key:
                        while values[0] == 'LOCKED':
                            stop_game = True
                            print('DIVISION LOCKED! \nUNLOCK PREVIOUS DIVISION FIRST')
                            break


    level_button = False
    while not level_button:
        print('LEVEL1 \nLEVEL2 \nLEVEL3 \nLEVEL4 \nLEVEL5 \nLEVEL6')
        GameOn = False
        while not GameOn:
            if game_state_loaded is True:
                pass
            else:
                player.game_level = int(input('ENTER LEVEL NUMBER TO SELECT THE LEVEL:  '))
                stop_game2 = False
                level_security()
                if stop_game == True:
                    continue
            player.save_game()
            print('LEVEL %d>>>' % player.game_level)
            while player.game_level <= 6:
                for num in range(1, 7):
                    for num2 in range(1, 51):
                        if player.game_level == num:
                            print('DIVISION %d' % num2, end=' ')
                print()
                stop_game2 = True
                if game_state_loaded is True:
                    pass
                else:
                    player.game_division = int(input('ENTER DIVISION NUMBER TO SELECT THE DIVISION:  '))
                    level_security()
                    if stop_game == True:
                        continue
                player.save_game()
                ExitForLoop = False
                for num in range(1, 51):
                    if ExitForLoop == True:
                        break
                    for num in range(1, 51):
                        if player.game_division == num:
                            print('LEVEL %d; DIVISION %d BEGINS>>>' % (
                                player.game_level, num)) if game_state_loaded != True else print(
                                'CONTINUING FROM LAST MEMORY... \nLEVEL %d; DIVISION %d>>>' % (
                                    player.game_level, num))
                            player.save_game()
                    ExitForLoop2 = False
                    for key, value in game_Level_WordLength_dict.items():
                        if ExitForLoop2 == True:
                            break
                        if player.game_level == key:
                            if game_state_loaded is True and '_' in player.gap_str:
                                player.game_word
                            else:
                                player.game_word = choice(Word_collection).upper()
                            player.save_game()
                            while len(player.game_word) not in value[1]:
                                if game_state_loaded is True and '_' in player.gap_str:
                                    player.game_word
                                else:
                                    player.game_word = choice(Word_collection).upper()
                                player.save_game()
                            else:
                                Quit = False
                                while not Quit:
                                    for round in range(11 - player.game_rounds):
                                        print('ROUND %d>>>' % player.game_rounds)
                                        for key, value in game_Level_WordLength_dict.items():
                                            if player.game_level == key:
                                                if game_state_loaded is True and '_' in player.gap_str:
                                                    player.game_word
                                                else:
                                                    player.game_word = choice(Word_collection).upper()
                                                player.save_game()
                                                while len(player.game_word) not in value[1]:
                                                    if game_state_loaded is True and '_' in player.gap_str:
                                                        player.game_word
                                                    else:
                                                        player.game_word = choice(
                                                            Word_collection).upper()
                                                    player.save_game()
                                        Description_Dict = {'NOUN': Noun, 'VERB': Verb,
                                                            'ADJECTIVE': Adjective, 'ADVERB': Adverb,
                                                            'SPORT': Sport,
                                                            'FOOD/FRUIT': Food_Fruit,
                                                            'COUNNTRY/CITY': Country_City,
                                                            'SCHOOL': School,
                                                            'BODY': Body,
                                                            'CALENDER/TIME': Calendar_Time,
                                                            'PROFESSION': Profession, 'MUSIC': Music,
                                                            'BEACH': Beach, 'FAMILY': Family,
                                                            'FLOWER': Flower, 'COLOUR': Colour}
                                        word_list = list(player.game_word)
                                        if game_state_loaded is True and '_' in player.gap_str:
                                            player.word_gap
                                        else:
                                            player.word_gap = ('_' * len(player.game_word))
                                        if game_state_loaded is True and '_' in player.gap_str:
                                            player.gap_str
                                        else:
                                            player.gap_str = '   '.join(player.word_gap)
                                        if game_state_loaded is True and '_' in player.gap_str:
                                            player.word_gap
                                        else:
                                            player.word_gap = list(player.word_gap)
                                        if game_state_loaded is True and '_' in player.gap_str:
                                            player.tries
                                        else:
                                            player.tries = 0
                                        
                                        player.save_game()
                                        while player.tries < player.game_max_trial:
                                            def obt_key(val):
                                                for key, value in Description_Dict.items():
                                                    if val == value:
                                                        return key


                                            for item in Description_Dict.values():
                                                if player.game_word.lower() in item or player.game_word.capitalize() in item:
                                                    print('WORD DESCRIPTION:  ', obt_key(item))
                                            print(player.gap_str)
                                            player.save_game()
                                            print()
                                            
                                            hint = input(
                                                "GET HINT? \nENTER 'Y' OR 'y' TO CONFIRM OTHERWISE, PRESS ANY KEY:   ")
                                            if hint == 'y' or hint == 'Y':
                                                if player.coins >= 10:
                                                    get_hint()
                                                    player.gap_str = '   '.join(player.word_gap)
                                                    player.coins -= 10
                                                    player.save_game()
                                                    print('COINS LEFT:  ', player.coins)

                                                    if '_' not in player.gap_str:
                                                        print(player.gap_str)
                                                        player.save_game()
                                                        win_comment = ['BRILLIANT!', 'AWESOME!',
                                                                        'BRAVO!', 'GREAT!',
                                                                        'ASTONISHING!',
                                                                        'EYE-WATERING!',
                                                                        'FANTASTIC!', 'WOW!',
                                                                        'OUTSTANDING!', 'OUTRAGEOUS!',
                                                                        'EXTRAORDINARY!',
                                                                        'WHOA!',
                                                                        'CONGRATULATIONS!']
                                                        print(choice(win_comment))
                                                        player.wins += 1
                                                        # player.game_rounds += 1
                                                        player.save_game()
                                                        print('WINS:  ', player.wins)
                                                        player.streak += 1
                                                        player.save_game()
                                                        print('STREAK: ', player.streak)
                                                        if player.streak % 5 == 0:
                                                            streak_comment = [
                                                                '%d IN A ROW!' % player.streak,
                                                                '%d IN %d!' % (
                                                                    player.streak, player.streak),
                                                                'CONSECUTIVE %d WINS!' % player.streak,
                                                                '%d AT ONCE!' % player.streak]
                                                            print(choice(streak_comment))
                                                            if player.game_division_dict[
                                                                player.game_division][
                                                                2] == 'NOT PLAYED':
                                                                player.coins += 5
                                                                print('YOU EARNED 5 COINS!\t COINS:  ',
                                                                        player.coins)
                                                            else:
                                                                pass
                                                            player.save_game()
                                                        else:
                                                            if player.game_division_dict[
                                                                player.game_division][
                                                                2] == 'NOT PLAYED':
                                                                player.coins += 1
                                                                print('YOU EARNED A COIN!\t COINS:  ',
                                                                        player.coins)
                                                            else:
                                                                pass
                                                            player.save_game()

                                                        Exit = input(
                                                            'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                                        if Exit == '1':
                                                            end_game()
                                                            game_state_loaded = False
                                                            player.save_game()
                                                            break
                                                        else:
                                                            score = ('SCORE:  %d / %d' % (
                                                                player.wins, player.game_rounds))
                                                            print('SCORE:  ', score)
                                                            player.game_rounds += 1
                                                            game_state_loaded = False
                                                            player.save_game()
                                                            break
                                                else:
                                                    print('INSUFFICIENT COINS!')
                                                    player.save_game()
                                                    pass

                                            else:
                                                guess = (input('Your guess?  ')).upper()
                                                player.save_game()
                                                if guess in player.game_word:
                                                    index = (
                                                        [pos for pos, letter in
                                                            enumerate(player.game_word)
                                                            if letter == guess])
                                                    for element in index:
                                                        player.word_gap[element] = guess
                                                        player.save_game()
                                                    player.gap_str = '   '.join(player.word_gap)
                                                    player.save_game()
                                                    if '_' not in player.gap_str:
                                                        print(player.gap_str)
                                                        player.save_game()
                                                        win_comment = ['BRILLIANT!', 'AWESOME!',
                                                                        'BRAVO!', 'GREAT!',
                                                                        'ASTONISHING!',
                                                                        'EYE-WATERING!', 'FANTASTIC!',
                                                                        'WOW!', 'OUTSTANDING!',
                                                                        'OUTRAGEOUS!',
                                                                        'EXTRAORDINARY!', 'WHOA!',
                                                                        'CONGRATULATIONS!']
                                                        print(choice(win_comment))
                                                        player.wins += 1
                                                        player.save_game()
                                                        print('WINS:  ', player.wins)
                                                        player.streak += 1
                                                        player.save_game()
                                                        print('STREAK: ', player.streak)
                                                        if player.streak % 5 == 0:
                                                            streak_comment = [
                                                                '%d IN A ROW!' % player.streak,
                                                                '%d IN %d!' % (
                                                                    player.streak, player.streak),
                                                                'CONSECUTIVE %d WINS!' % player.streak,
                                                                '%d AT ONCE!' % player.streak]
                                                            print(choice(streak_comment))
                                                            if player.game_division_dict[
                                                                player.game_division][
                                                                2] == 'NOT PLAYED':
                                                                player.coins += 5
                                                                print('YOU EARNED 5 COINS!\t COINS:  ',
                                                                        player.coins)
                                                            else:
                                                                pass
                                                            player.save_game()
                                                        else:
                                                            if player.game_division_dict[
                                                                player.game_division][
                                                                2] == 'NOT PLAYED':
                                                                player.coins += 1
                                                                print('YOU EARNED A COIN!\t COINS:  ',
                                                                        player.coins)
                                                            else:
                                                                pass
                                                            player.save_game()
                                                        print(player.gap_str)

                                                        Exit = input(
                                                            'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                                        if Exit == '1':
                                                            end_game()
                                                            game_state_loaded = False
                                                            player.save_game()
                                                            GameOn = True
                                                            ExitForLoop = True
                                                            ExitForLoop2 = True
                                                            Quit = True
                                                            player.save_game()
                                                            break
                                                        else:
                                                            score = ('SCORE:  %d / %d' % (
                                                                player.wins, player.game_rounds))
                                                            print('SCORE:  ', score)
                                                            player.game_rounds += 1
                                                            game_state_loaded = False
                                                            player.save_game()
                                                            break

                                                else:
                                                    player.tries += 1
                                                    player.save_game()
                                                    print(guess, 'is not in the word')

                                        else:
                                            print('MAN HANGED!!!')
                                            print(
                                                'You\'re out of tries \nGAME OVER! \nThe word is \'%s\'' % player.game_word)
                                            revival = input(
                                                "REVIVE MAN? \nEnter 'y' or 'Y' to confirm otherwise, press any key:  ")
                                            if revival in ['y', 'Y']:
                                                if player.coins >= player.game_revival_coins:
                                                    print('MAN REVIVED!!!')
                                                    player.tries -= player.game_max_trial
                                                    player.save_game()
                                                    player.coins -= player.game_revival_coins
                                                    player.save_game()
                                                    player.game_revival_coins += 10
                                                    player.save_game()
                                                    print('REMAINING COINS:  ', player.coins)
                                                    continue
                                                else:
                                                    print('INSUFFICIENT COINS!')
                                                    player.losses += 1
                                                    player.save_game()
                                                    if player.streak > 0:
                                                        player.streak = 0
                                                        player.save_game()
                                                        print('STREAK ENDS!')
                                                        print('LOSES: ', player.losses)

                                                    Exit = input(
                                                        'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                                    if Exit == '1':
                                                        option_made = True
                                                        end_game()
                                                        GameOn = True
                                                        ExitForLoop = True
                                                        ExitForLoop2 = True
                                                        Quit = True
                                                        game_state_loaded = False
                                                        player.save_game()
                                                        break
                                                    else:
                                                        option_made = True
                                                        score = ('%d/%d' % (
                                                            player.wins, player.game_rounds))
                                                        print('SCORE:  ', score)
                                                        player.game_rounds += 1
                                                        game_state_loaded = False
                                                        player.save_game()
                                                        continue


                                            else:
                                                player.losses += 1
                                                player.save_game()
                                                if player.streak > 0:
                                                    player.streak = 0
                                                    player.save_game()
                                                    print('STREAK ENDS!')
                                                    print('LOSES: ', player.losses)

                                                Exit = input(
                                                    'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS '
                                                    'ANY KEY TO CONTINUE:')
                                                if Exit == '1':
                                                    end_game()
                                                    GameOn = True
                                                    ExitForLoop = True
                                                    ExitForLoop2 = True
                                                    Quit = True
                                                    game_state_loaded = False
                                                    player.save_game()
                                                    break
                                                else:
                                                    score = ('%d/%d' % (
                                                        player.wins, player.game_rounds))
                                                    print('SCORE:  ', score)
                                                    player.game_rounds += 1
                                                    game_state_loaded = False
                                                    player.save_game()

                                    else:
                                        if player.wins in [5, 6]:
                                            division_rating = 1
                                            print('YOU WON THIS DIVISION WITH 1 STAR')
                                        elif player.wins in [7, 8, 9]:
                                            division_rating = 2
                                            print('YOU WON THIS DIVISION WITH 2 STARS')
                                        elif player.wins in [10]:
                                            division_rating = 3
                                            print('YOU WON THIS DIVISION WITH 3 STARS')
                                        else:
                                            print(
                                                'YOU CAN\'T CONTINUE TO THE NEXT DIVISION AS THE MINIMUM WIN REQUIRED IS 5')
                                            player.streak = 0
                                            player.wins = 0
                                            player.losses = 0
                                            player.game_rounds = 1
                                            ExitForLoop = True
                                            ExitForLoop2 = True
                                            Quit = True
                                            game_state_loaded = False
                                            player.save_game()
                                            break
                                        player.game_division_dict[player.game_division][2] = 'PLAYED'
                                        game_state_loaded = False
                                        player.save_game()
                                        player.game_division_dict[player.game_division][
                                            1] = division_rating
                                        player.game_division += 1
                                        player.game_division_dict[player.game_division][0] = 'UNLOCKED'
                                        player.save_game()
                                        if player.game_division > 50:
                                            print(
                                                'LEVEL %d IS FINISHED! \nNEXT LEVEL>>>' % player.game_level) if player.game_level != 6 else print(
                                                'CONGRATUTLATIONS! \nYOU\'VE REACHED THE END OF THE HANGMAN GAME\'S CAREER MODE...')
                                            player.streak = 0
                                            player.wins = 0
                                            player.losses = 0
                                            player.coins += 7
                                            print('YOU EARNED 7 COOL COINS!')
                                            player.game_rounds = 1
                                            player.game_level += 1
                                            player.save_game()
                                            for key, values in game_Level_WordLength_dict.items():
                                                if player.game_level == key:
                                                    values[0] = 'UNLOCKED'
                                            if player.game_level <= 6:
                                                print('LEVEL %d IS UNLOCKED' % player.game_level)
                                            else:
                                                pass
                                            player.save_game()
                                            ExitForLoop = True
                                            ExitForLoop2 = True
                                            Quit = True
                                            player.save_game()
                                            break

                                        else:
                                            print('DIVISION %d IS UNLOCKED' % player.game_division)
                                            player.streak = 0
                                            player.wins = 0
                                            player.losses = 0
                                            player.coins += 5
                                            print('YOU EARNED 5 COOL COINS! \nCOINS:  ', player.coins)
                                            player.game_rounds = 1
                                            game_state_loaded = False
                                            player.save_game()
                                            break