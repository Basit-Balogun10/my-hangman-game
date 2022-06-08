import pickle

class Player:
    def __init__(self, name=None, game_difficulty=None, game_max_trial=None, game_level=None,
                    game_Level_WordLength_dict=None, game_division=None, game_division_dict=None,
                    game_division_rating=None, game_rounds=None, wins=None, losses=None, streak=None, coins=None,
                    game_word=None, word_gap=None, gap_str=None, tries=None, game_revival_coins=None):
        self.name = name
        self.game_difficulty = game_difficulty
        self.game_max_trial = game_max_trial
        self.game_level = game_level
        self.game_Level_WordLength_dict = game_Level_WordLength_dict
        self.game_division = game_division
        self.game_division_dict = game_division_dict
        self.game_rounds = game_rounds
        self.wins = wins
        self.losses = losses
        self.streak = streak
        self.coins = coins
        self.game_word = game_word
        self.word_gap = word_gap
        self.gap_str = gap_str
        self.tries = tries
        self.game_revival_coins = game_revival_coins
        self.state_file = 'game_state.txt'

    def save_game(self):
        global player
        with open(self.state_file, 'wb') as save_state:
            pickle.dump(player, save_state)

    def load_game(self):
        global player
        with open(self.state_file, 'rb') as load_state:
            player = pickle.load(load_state)

    def __str__(self):
        return '{} is playing game at {} difficulty level; level {}, division{} round {} with {} wins, {} losses, {}streaks, and {}coins; Used trials on current word: {}'.format(
            self.name, self.game_difficulty, self.game_level, self.game_division, self.game_rounds, self.wins,
            self.losses, self.streak, self.coins, self.tries)


class SinglePlayer(Player):
    def __init__(self, game_rounds=None, game_difficulty=None, game_max_trial=None, wins=None, losses=None,
                    streak=None, coins=None, category_selection=None,
                    game_word=None, word_gap=None, gap_str=None, tries=None, game_revival_coins=None):
        super().__init__(game_difficulty, game_max_trial, wins, losses, streak, coins, game_word, word_gap, gap_str,
                            tries, game_revival_coins)
        self.game_rounds = game_rounds
        self.category_selection = category_selection

    def save_game(self, description):
        global RS_player, CS_player
        if description == 'random':
            self.object = RS_player
            self.state_file = 'RSP_game_state.txt'
        elif description == 'category':
            self.object = CS_player
            self.state_file = 'CSP_game_state.txt'
        with open(self.state_file, 'wb') as save_state:
            pickle.dump(self.object, save_state)

    def load_game(self, description):
        global RS_player, CS_player
        if description == 'random':
            self.object = RS_player
            self.state_file = 'RSP_game_state.txt'
        elif description == 'category':
            self.object = CS_player
            self.state_file = 'CSP_game_state.txt'
        with open(self.state_file, 'rb') as load_state:
            self.object = pickle.load(load_state)
            if description is 'random':
                RS_player = self.object
            else:
                CS_player = self.object

    def __str__(self):
        return 'Game has been resumed at round {}, difficulty level {}. Player has {} wins, {} losses, {}streaks, and {}coins; Used trials on current word: {}'.format(
            self.game_rounds,
            self.game_difficulty, self.wins, self.losses, self.streak, self.coins, self.tries)


class MultiPlayer(Player):
    def __init__(self, name=None, game_rounds=None, game_difficulty=None, game_max_trial=None,
                    count=None, streak=None, coins=None, game_word=None, word_gap=None, gap_str=None, tries=None,
                    name2=None, count2=None, streak2=None, coins2=None,
                    counts=None, counts_neutral=None, names=None, names_neutral=None, coins_list=None,
                    coins_neutral=None, streaks=None, streaks_neutral=None, category_selection=None):
        global PVP_MP, RM_player, CM_player
        super().__init__(name, game_difficulty, game_max_trial, streak, coins, game_word, word_gap,
                            gap_str, tries)
        self.count = count
        self.counts = counts
        self.counts_neutral = counts_neutral
        self.names = names
        self.names_neutral = names_neutral
        self.coins_list = coins_list
        self.coins_neutral = coins_neutral
        self.streaks = streaks
        self.streaks_neutral = streaks_neutral
        self.game_rounds = game_rounds
        self.category_selection = category_selection
        self.name2 = name2
        self.count2 = count2
        self.streak2 = streak2
        self.coins2 = coins2

    def save_game(self, description):
        global PVP_MP, RM_player, CM_player
        if description == 'pvp':
            self.object = PVP_MP
            self.state_file = 'PVP_MP_game_state.txt'
        elif description == 'random':
            self.object = RM_player
            self.state_file = 'RMP_game_state.txt'
        elif description == 'category':
            self.object = 'CM_player'
            self.state_file = 'CMP_game_state.txt'
        with open(self.state_file, 'wb') as save_state:
            pickle.dump(self.object, save_state)

    def load_game(self, description):
        global PVP_MP, RM_player, CM_player
        if description == 'pvp':
            self.object = PVP_MP
            self.state_file = 'PVP_MP_game_state.txt'
        elif description == 'random':
            self.object = RM_player
            self.state_file = 'RMP_game_state.txt'
        elif description == 'category':
            self.object = 'CM_player'
            self.state_file = 'CMP_game_state.txt'
        with open(self.state_file, 'rb') as load_state:
            self.object = pickle.load(load_state)
            if description is 'random':
                RM_player = self.object
            elif description is 'category':
                CM_player = self.object
            elif description is 'pvp':
                PVP_MP = self.object
        print(RM_player)

    def __str__(self):
        return (
            'Game has been resumed at at round {}, difficulty level {}:\n{}(P1) has {} points, {}streaks, and {}coins '
            '\n{}(P2) has {} points, {}streaks, and {}coins; Used trials on current word: {}'.format(self.game_rounds,
                                                                        self.game_difficulty, self.name,
                                                                        self.count, self.streak,
                                                                        self.coins, self.name2,
                                                                        self.count2, self.streak2, self.coins2, self.tries))

