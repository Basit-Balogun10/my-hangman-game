from random import choice
from word_collection import *
from utils.difficulty_level import set_difficulty_level
from players import MultiPlayer

def play_random_multiplayer():
    RM_player = MultiPlayer()
    load_request = input('A- NEW GAME \nB- LOAD GAME')
    if load_request.upper() == 'B':
        try:
            RM_player.load_game('random')
            print('SAVED STATE LOADED')
            game_state_loaded = True
            print(RM_player)
        except FileNotFoundError as f:
            print('SAVED STATE FILE NOT FOUND')
            game_state_loaded = False
            set_difficulty_level(RM_player)
            RM_player.names = [RM_player.name, RM_player.name2]
            RM_player.count = 0
            RM_player.count2 = 0
            RM_player.streak = 0
            RM_player.streak2 = 0
            RM_player.coins = 0
            RM_player.coins2 = 0
            RM_player.game_rounds = 1
            RM_player.coins_list = [RM_player.coins, RM_player.coins2]
            RM_player.streaks = [RM_player.streak, RM_player.streak2]
            RM_player.counts = [RM_player.count, RM_player.count2]
            RM_player.save_game('random')
    elif load_request.upper() == 'A':
        game_state_loaded = False
        try:
            with open('RMP_game_state.txt', 'w'):
                pass
        except FileNotFoundError:
            pass
        set_difficulty_level(RM_player)
        RM_player.names = [RM_player.name, RM_player.name2]
        RM_player.count = 0
        RM_player.count2 = 0
        RM_player.streak = 0
        RM_player.streak2 = 0
        RM_player.coins = 0
        RM_player.coins2 = 0
        RM_player.game_rounds = 1
        RM_player.coins_list = [RM_player.coins, RM_player.coins2]
        RM_player.streaks = [RM_player.streak, RM_player.streak2]
        RM_player.counts = [RM_player.count, RM_player.count2]
        RM_player.save_game('random')
    if game_state_loaded is False:
        RM_player.name = input('PLAYER1-->Please enter your name:  ').upper()
        print('WELCOME %s!' % RM_player.name.upper())
        RM_player.name2 = input('PLAYER2-->Please enter your name:  ').upper()
        print('WELCOME %s!' % RM_player.name2.upper())
        if RM_player.name is '':
            RM_player.name = 'Player1'
        if RM_player.name2 is '':
            RM_player.name2 = 'Player2'
        RM_player.names[0] = RM_player.name
        RM_player.names[1] = RM_player.name2
    else:
        pass


    def get_hint():
        help = choice(word_list)
        while help in RM_player.gap_str:
            help = choice(word_list)
        for letter in word_list:
            index = ([pos for pos, letter in enumerate(word_list) if letter == help])
            for element in index:
                RM_player.word_gap[element] = help


    def end_game():
        print('GAME OVER!')
        score = ("(%s)%d : (%s)%d" % (
        RM_player.names[0], RM_player.counts[0], RM_player.names[1], RM_player.counts[1]))
        print('SCORE:  ', score)


    quit = False
    while not quit:
        cycle = 1
        recycle = False
        while not recycle:
            if True:
                Continue = False
                if game_state_loaded is False:
                    RM_player.names_neutral = RM_player.names[1]
                    RM_player.names[1] = RM_player.names[0]
                    RM_player.names[0] = RM_player.names_neutral
                    RM_player.coins_neutral = RM_player.coins_list[1]
                    RM_player.coins_list[1] = RM_player.coins_list[0]
                    RM_player.coins_list[0] = RM_player.coins_neutral
                    RM_player.streaks_neutral = RM_player.streaks[1]
                    RM_player.streaks[1] = RM_player.streaks[0]
                    RM_player.streaks[0] = RM_player.streaks_neutral
                    RM_player.counts_neutral = RM_player.counts[1]
                    RM_player.counts[1] = RM_player.counts[0]
                    RM_player.counts[0] = RM_player.counts_neutral
            if game_state_loaded is False:
                RM_player.game_word = choice(Word_collection).upper()
            else:
                pass
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
                word_list = list(RM_player.game_word)
            else:
                pass
            if game_state_loaded is False:
                RM_player.word_gap = ('_' * len(RM_player.game_word))
            else:
                pass
            if game_state_loaded is False:
                RM_player.gap_str = '   '.join(RM_player.word_gap)
            else:
                pass
            if game_state_loaded is False:
                RM_player.word_gap = list(RM_player.word_gap)
            else:
                pass
            if game_state_loaded is False:
                RM_player.tries = 0
            else:
                pass
            if game_state_loaded is False:
                RM_player.save_game('random')
            else:
                pass

            RM_player.tries = 0
            print('%s TURN....' % RM_player.names[1])
            print('ROUND %d>>>' % RM_player.game_rounds)
            while RM_player.tries < RM_player.game_max_trial:
                RM_player.save_game('random')


                def obt_key(val):
                    for key, value in Description_Dict.items():
                        if val == value:
                            return key


                for item in Description_Dict.values():
                    if RM_player.game_word.lower() in item or RM_player.game_word.capitalize() in item:
                        print('WORD DESCRIPTION:  ', obt_key(item))
                print(RM_player.gap_str)
                print()
                RM_player.save_game('random')
                hint = input(
                    "GET HINT? \nENTER 'Y' OR 'y' TO CONFIRM OTHERWISE, PRESS ANY KEY:   ")
                if hint == 'y' or hint == 'Y':
                    if RM_player.coins_list[1] >= 3:
                        get_hint()
                        RM_player.gap_str = '   '.join(RM_player.word_gap)
                        RM_player.coins_list[1] -= 3
                        print('%s, YOUR COINS LEFT:  %d' % (
                        RM_player.names[1], RM_player.coins_list[1]))
                        RM_player.save_game('random')
                        if '_' not in RM_player.gap_str:
                            print(RM_player.gap_str)
                            win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                            'ASTONISHING!',
                                            'EYE-WATERING!',
                                            'FANTASTIC!', 'WOW!', 'OUTSTANDING!',
                                            'OUTRAGEOUS!',
                                            'EXTRAORDINARY!',
                                            'WHOA!',
                                            'CONGRATULATIONS!']
                            print(choice(win_comment))
                            RM_player.counts[1] += 1
                            print('POINTS:  ', RM_player.counts[1])
                            RM_player.streaks[1] += 1
                            print("%s STREAK:  %d" % (
                            RM_player.names[1], RM_player.streaks[1]))
                            RM_player.save_game('random')
                            if RM_player.streaks[1] % 5 == 0:
                                streak_comment = ['%d IN A ROW!' % RM_player.streaks[1],
                                                    '%d IN %d!' % (RM_player.streaks[1],
                                                                    RM_player.streaks[1]),
                                                    'CONSECUTIVE %d WINS!' %
                                                    RM_player.streaks[1],
                                                    '%d AT ONCE!' % RM_player.streaks[1]]
                                print(choice(streak_comment))
                                RM_player.coins_list[1] += 5
                                print('%s EARNED 5 COINS!\tCOINS:  %d' % (
                                RM_player.names[1], RM_player.coins_list[1]))
                                RM_player.tries = 10
                                Continue = True
                                break
                            else:
                                RM_player.coins_list[1] += 1
                                print('%s EARNED A COIN!\tCOINS:  %d' % (
                                RM_player.names[1], RM_player.coins_list[1]))
                                RM_player.tries = 10
                                Continue = True
                                break
                            RM_player.save_game('random')
                    else:
                        print('INSUFFICIENT COINS!')
                        RM_player.save_game('random')
                else:
                    guess = input('Your guess, %s?:  ' % RM_player.names[1]).upper()
                    RM_player.save_game('random')
                    if guess in RM_player.game_word:
                        index = ([pos for pos, letter in enumerate(RM_player.game_word) if
                                    letter == guess])
                        for element in index:
                            RM_player.word_gap[element] = guess
                            RM_player.gap_str = '   '.join(RM_player.word_gap)
                            RM_player.save_game('random')
                            if '_' not in RM_player.gap_str:
                                print(RM_player.gap_str)
                                win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                                'ASTONISHING!',
                                                'EYE-WATERING!',
                                                'FANTASTIC!', 'WOW!', 'OUTSTANDING!',
                                                'OUTRAGEOUS!',
                                                'EXTRAORDINARY!', 'WHOA!',
                                                'CONGRATULATIONS!']
                                print(choice(win_comment))
                                RM_player.counts[1] += 1
                                RM_player.streaks[1] += 1
                                print("%s STREAK:  %d" % (
                                RM_player.names[1], RM_player.streaks[1]))
                                RM_player.save_game('random')
                                if RM_player.streaks[1] % 5 == 0:
                                    streak_comment = ['%d IN A ROW!' % RM_player.streaks[1],
                                                        '%d IN %d!' % (RM_player.streaks[1],
                                                                        RM_player.streaks[1]),
                                                        'CONSECUTIVE %d WINS!' %
                                                        RM_player.streaks[1],
                                                        '%d AT ONCE!' % RM_player.streaks[1]]
                                    print(choice(streak_comment))
                                    RM_player.coins_list[1] += 5
                                    print('%s EARNED 5 COINS!\tCOINS:  %d' % (
                                        RM_player.names[1], RM_player.coins_list[1]))
                                    RM_player.tries = 10
                                    Continue = True
                                    break
                                else:
                                    RM_player.coins_list[1] += 1
                                    print('%s EARNED A COIN!\tCOINS:  %d' % (
                                        RM_player.names[1], RM_player.coins_list[1]))
                                    RM_player.tries = 10
                                    Continue = True
                                    break
                                RM_player.save_game('random')

                    else:
                        RM_player.tries += 1
                        print(guess, 'is not in the word')
                        RM_player.save_game('random')
            else:
                if Continue == False:
                    print('MAN HANGED!!!')
                    print(
                        'You\'re out of tries \nYOU LOST! \nThe hidden word is \'%s\'' % RM_player.game_word)
                    RM_player.save_game('random')
            if cycle % 2 == 0:
                RM_player.name2 = RM_player.names[1]
                RM_player.coins2 = RM_player.coins_list[1]
                RM_player.count2 = RM_player.counts[1]
                RM_player.streak2 = RM_player.streaks[1]
                Exit = input(
                    'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                if Exit == '1':
                    end_game()
                    quit = True
                    game_state_loaded = False
                    RM_player.save_game('random')
                    break
                else:
                    score = ("(%s)%d : (%s)%d" % (
                    RM_player.names[0], RM_player.counts[0], RM_player.names[1],
                    RM_player.counts[1]))
                    print('SCORE:  ', score)
                    RM_player.game_rounds += 1
                    game_state_loaded = False
                    RM_player.save_game('random')
                    break
            else:
                RM_player.name = RM_player.names[1]
                RM_player.coins = RM_player.coins_list[1]
                RM_player.count = RM_player.counts[1]
                RM_player.streak = RM_player.streaks[1]
                cycle += 1
                game_state_loaded = False
                RM_player.save_game('random')