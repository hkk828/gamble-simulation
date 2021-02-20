import random

class martingale:
    '''
    Martingale strategy (or martingale) is a betting strategy that doubles the bet when losing the game,
    and sets it to default bet when winning the game. It is usually used for blackjack or roulette.
    This is the class for more general martinagale, which one can change the probability of winning the game,
    starting money, default bet size, and the multiplication factor when losing the game.
    '''

    def __init__(self, win_prob=18/37, asset=1024, default_bet=1, ratio=2):
        '''
        win_prob: probability of winning the bet, which should be in (0,1]
        asset: initial asset for the gamble (default value is 1024, which is the 10th power of 2), > 0
        default_bet: lowest bet of the martingale strategy (default value is 1), > 0
        ratio: multiplication factor when losing the bet (default value is 2), > 1
        '''
        self.win_prob = win_prob
        self.asset = asset             # keeps track of the remaining money
        self.default_bet = default_bet
        self.current_bet = default_bet         # current bet size
        self.ratio = ratio

    def getAsset(self):
        ''' returns the current asset '''
        return self.asset

    def _bet(self):
        '''
        Returns the asset after the single bet and the result. (0: lose, 1: win)
        If the current bet size is bigger than the current asset than it returns None.
        '''
        if self.current_bet > self.asset:
            return None, None
        
        winning = random.random() < self.win_prob
        # if winning the bet, add the current bet on the asset and set the bet as default bet
        if winning:
            self.asset += self.current_bet
            self.current_bet = self.default_bet
        # if losing the bet, subtract the current bet from the asset and multiply the bet by the ratio
        else:
            self.asset -= self.current_bet
            self.current_bet *= self.ratio

        return self.asset, winning

    def bet(self, n_trial):
        ''' 
        Returns the tuple of the list of 'n_trial+1(starting asset)' results
        and the number of maximum consecutive loses.
        If a bet is no more possible, then the returned result contains only the proper (shortened) result.
        '''
        asset_history = [self.asset]

        last_bet = None             # result of the last bet -> 0: lose, 1: win
        max_consecutive_lose = 0
        temp_consecutive_lose = 0

        for _ in range(n_trial):
            betted, current_bet = self._bet()
            if betted:
                asset_history.append(betted)

                if current_bet == last_bet == 0:
                    temp_consecutive_lose += 1
                else:
                    # if lost the current bet, start counting lose from 1
                    if current_bet == 0:
                        temp_consecutive_lose = 1
                    # if won the current bet, update lose count and set it to 0
                    else:
                        max_consecutive_lose = max(temp_consecutive_lose, max_consecutive_lose)
                        temp_consecutive_lose = 0
                
                last_bet = current_bet
            else:
                break

        # update lose count once more, just in case the loop ended without updating
        max_consecutive_lose = max(temp_consecutive_lose, max_consecutive_lose)

        return asset_history, max_consecutive_lose