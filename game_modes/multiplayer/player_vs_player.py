from random import choice
from os import system

def play_player_vs_player_mode():
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



    quit = False
    while not quit:
        cycle = 1
        recycle = False
        while not recycle:
            if True:
                Continue = False
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

            word = input('%s, Please enter your word:  ' % Players[1]).upper()
            word_description = input("%s, Give the word description(OPTIONAL):  " % Players[1])
            system('cls')
            word_list = list(word)
            gap = ('_' * len(word))
            gap_str = '   '.join(gap)
            gap = list(gap)

            tries = 0
            print('%s TURN....' % Players[0])
            while tries < 9:
                print(
                    'WORD DESCRIPTION:  %s' % word_description) if word_description is not '' else print(
                    'WORD DESCRIPTION:  NOT PROVIDED')
                print(gap_str)
                hint = input(
                    "GET HINT? \nENTER 'Y' OR 'y' TO CONFIRM OTHERWISE, PRESS ANY KEY:   ")
                if hint == 'y' or hint == 'Y':
                    if coins[0] >= 3:
                        get_hint()
                        gap_str = '   '.join(gap)
                        coins[0] -= 3
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
                            counts[0] += 1
                            print('POINTS:  ', counts[0])
                            streaks[0] += 1
                            print("%s STREAK:  %d" % (Players[0], streaks[0]))
                            if streaks[0] % 5 == 0:
                                streak_comment = ['%d IN A ROW!' % streaks[0],
                                                    '%d IN %d!' % (streaks[0], streaks[0]),
                                                    'CONSECUTIVE %d WINS!' % streaks[0],
                                                    '%d AT ONCE!' % streaks[0]]
                                print(choice(streak_comment))
                                coins[0] += 5
                                print('%s EARNED 5 COINS!\tCOINS:  %d' % (Players[0], coins[0]))
                                tries = 10
                                Continue = True
                                break
                            else:
                                coins[0] += 1
                                print('%s EARNED A COIN!\tCOINS:  %d' % (Players[0], coins[0]))
                                tries = 10
                                Continue = True
                                break
                    else:
                        print('INSUFFICIENT COINS!')
                else:
                    guess = input('Your guess, %s?:  ' % Players[0]).upper()
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
                                                'EXTRAORDINARY!', 'WHOA!',
                                                'CONGRATULATIONS!']
                                print(choice(win_comment))
                                counts[0] += 1
                                streaks[0] += 1
                                print("%s STREAK:  %d" % (Players[0], streaks[0]))
                                if streaks[0] % 5 == 0:
                                    streak_comment = ['%d IN A ROW!' % streaks[0],
                                                        '%d IN %d!' % (streaks[0], streaks[0]),
                                                        'CONSECUTIVE %d WINS!' % streaks[0],
                                                        '%d AT ONCE!' % streaks[0]]
                                    print(choice(streak_comment))
                                    coins[0] += 5
                                    print('%s EARNED 5 COINS!\tCOINS:  %d' % (
                                        Players[0], coins[0]))
                                    tries = 10
                                    Continue = True
                                    break
                                else:
                                    coins[0] += 1
                                    print('%s EARNED A COIN!\tCOINS:  %d' % (
                                        Players[0], coins[0]))
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
            if cycle % 2 == 0:
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

                    break
            cycle += 1
