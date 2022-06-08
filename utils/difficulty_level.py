def set_difficulty_level(object):
        print('EASY--> A \nHARD--> B')
        global max_trial
        object.game_difficulty = input('Select game difficulty level: ')
        if object.game_difficulty.upper() == 'A':
            object.game_max_trial = 9
            print('MAXIMUM NUMBER OF ENTRY IS ', object.game_max_trial)
        elif object.game_difficulty.upper() == 'B':
            object.game_max_trial = 6
            print('MAXIMUM NUMBER OF ENTRY IS ', object.game_max_trial)
        else:
            print('INVALID ENTRY! \nMAXIMUM NUMBER OF ENTRY IS SET TO DEFAULT(9)')
            object.game_max_trial = 9

