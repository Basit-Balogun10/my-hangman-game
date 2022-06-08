from random import choice
from word_collection import *
from utils.difficulty_level import set_difficulty_level

def play_category_multiplayer():
    set_difficulty_level('player')
    Player1 = input('PLAYER1-->Please enter your name:  ').upper()
    print('WLECOME %s!' % Player1.upper())
    Player2 = input('PLAYER2-->Please enter your name:  ').upper()
    print('WLECOME %s!' % Player2.upper())
    Players = [Player1, Player2]
    count1 = 0
    count2 = 0
    streak1 = 0
    streak2 = 0
    coins1 = 0
    coins2 = 0
    rounds = 1
    coins = [coins1, coins2]
    streaks = [streak1, streak2]
    counts = [count1, count2]


    def get_hint():
        help = choice(word_list)
        while help in gap_str:
            help = choice(word_list)
        for letter in word_list:
            index = ([pos for pos, letter in enumerate(word_list) if letter == help])
            for element in index:
                gap[element] = help


    def end_game():
        print('GAME OVER!')
        score = ("(%s)%d : (%s)%d" % (Players[0], counts[0], Players[1], counts[1]))
        print('SCORE:  ', score)


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
    selection = input(
        "Please enter the corresponding value of the words category you'd like to play: ").upper()
    quit = False
    while not quit:
        Continue = False
        cycle = 1
        Players_neutral = Players[1]
        Players[1] = Players[0]
        Players[0] = Players_neutral
        coins_neutral = coins[1]
        coins[1] = coins[0]
        coins[0] = coins_neutral
        streaks_neutral = streaks[1]
        streaks[1] = streaks[0]
        streaks[0] = streaks_neutral
        counts_neutral = counts[1]
        counts[1] = counts[0]
        counts[0] = counts_neutral
        for keys, values in Description_Dict.items():
            if selection in keys:
                word_description = values[0]
                word = choice(values[1]).upper()
                word_list = list(word)
                gap = ('_' * len(word))
                gap_str = '   '.join(gap)
                gap = list(gap)
                tries = 0
        print('%s TURN....' % Players[1])
        while tries < max_trial:
            print('WORD DESCRIPTION:  ', word_description)
            print(gap_str)
            hint = input(
                "GET HINT? \nENTER 'Y' OR 'y' TO CONFIRM OTHERWISE, PRESS ANY KEY:   ")
            if hint == 'y' or hint == 'Y':
                if coins[1] >= 3:
                    get_hint()
                    gap_str = '   '.join(gap)
                    coins[1] -= 3
                    print('%s, YOUR COINS LEFT:  %d' % (Players[1], coins[1]))
                    if '_' not in gap_str:
                        print(gap_str)
                        win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                        'ASTONISHING!',
                                        'EYE-WATERING!',
                                        'FANTASTIC!', 'WOW!', 'OUTSTANDING!', 'OUTRAGEOUS!',
                                        'EXTRAORDINARY!',
                                        'WHOA!',
                                        'CONGRATULATIONS!']
                        print(choice(win_comment))
                        counts[1] += 1
                        print('POINTS:  ', counts[1])
                        streaks[1] += 1
                        print("%s STREAK:  %d" % (Players[1], streaks[1]))
                        if streaks[1] % 5 == 0:
                            streak_comment = ['%d IN A ROW!' % streaks[1],
                                                '%d IN %d!' % (streaks[1], streaks[1]),
                                                'CONSECUTIVE %d WINS!' % streaks[1],
                                                '%d AT ONCE!' % streaks[1]]
                            print(choice(streak_comment))
                            coins[1] += 5
                            print('%s EARNED 5 COINS!\tCOINS:  %d' % (Players[1], coins[1]))
                            tries = 10
                            Continue = True
                            break
                        else:
                            coins[1] += 1
                            print('%s EARNED A COIN!\tCOINS:  %d' % (Players[1], coins[1]))
                            tries = 10
                            Continue = True
                            break
                else:
                    print('INSUFFICIENT COINS!')
            else:
                guess = input('Your guess, %s?:  ' % Players[1]).upper()
                if guess in word:
                    index = ([pos for pos, letter in enumerate(word) if letter == guess])
                    for element in index:
                        gap[element] = guess
                        gap_str = '   '.join(gap)
                        if '_' not in gap_str:
                            print(gap_str)
                            win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                            'ASTONISHING!',
                                            'EYE-WATERING!',
                                            'FANTASTIC!', 'WOW!', 'OUTSTANDING!',
                                            'OUTRAGEOUS!',
                                            'EXTRAORDINARY!',
                                            'WHOA!',
                                            'CONGRATULATIONS!']
                            print(choice(win_comment))
                            counts[1] += 1
                            streaks[1] += 1
                            print("%s STREAK:  %d" % (Players[1], streaks[1]))
                            if streaks[1] % 5 == 0:
                                streak_comment = ['%d IN A ROW!' % streaks[1],
                                                    '%d IN %d!' % (streaks[1], streaks[1]),
                                                    'CONSECUTIVE %d WINS!' % streaks[1],
                                                    '%d AT ONCE!' % streaks[1]]
                                print(choice(streak_comment))
                                coins[1] += 5
                                print('%s EARNED 5 COINS!\tCOINS:  %d' % (
                                Players[1], coins[1]))
                                tries = 10
                                Continue = True
                                break
                            else:
                                coins[1] += 1
                                print('%s EARNED A COIN!\tCOINS:  %d' % (
                                Players[1], coins[1]))
                                tries = 10
                                Continue = True
                                break

                else:
                    tries += 1
                    print(guess, 'is not in the word')
        else:
            if Continue == False:
                print('MAN HANGED!!!')
                print('You\'re out of tries \nYOU LOST! \nThe hidden word is \'%s\'' % word)
        if Players[1] == Player2:
            Exit = input(
                'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
            if Exit == '1':
                end_game()
                quit = True
                break
            else:
                score = ("(%s)%d : (%s)%d" % (Players[0], counts[0], Players[1], counts[1]))
                print('SCORE:  ', score)
                rounds += 1
                print('ROUND %d>>>' % rounds)
        cycle += 1