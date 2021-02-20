from tqdm import tqdm
from utils.plot import betplot

class monteCarlo:

    def run(n_sim, betStrategy, n_trial, seed, save=False, dpi=None, show=True):
        '''
        Monte Carlo simulation with a given betting strategy.
        Returns a list of final asset at each simulation, a list of bankrupt simulation indices,
        and a list of max_consecutive_lose at each simulation.

        n_sim: int. number of simulations.
        betStrategy: object from strategy directory.
        n_trial: int. number of bets in a single simulation.
        seed: int. seed for random state.
        save: bool. checks whether you want to save the image.
        dpi: int. dpi for the image.
        show: bool. checks whether you want to see the image.
        '''
        initial_state = betStrategy.__dict__.copy()
        del initial_state['current_bet']    # delete internal attribute, which is not need for __init__
        strategy_name = type(betStrategy).__name__
        outcomes = []               # store final assets for each simulation
        bankruptcy = []             # store indices of bankrupt simulations
        max_consecutive_loses = []  # store maximum number of consecutive loses for each simulation

        for sim in tqdm(range(n_sim)):
            # bet n_trial times for each simulation
            bet_result = betStrategy.bet(n_trial)   # (asset_history, max_consecutive_lose)

            # save the plot of n_trial bet history
            # path is set to be 'imgs/{strategy_name}/{seed}_{sim}.png'
            path = f'imgs/{strategy_name}/{seed}_{sim}.png'
            betplot.history(bet_result=bet_result, save=save, dpi=dpi, path=path, show=show)

            # It goes bankrupt if the length of bet_result is shorter than (n_trial+1)
            if len(bet_result[0]) < n_trial + 1:
                bankruptcy.append(sim)

            outcomes.append(betStrategy.getAsset())
            max_consecutive_loses.append(bet_result[1])

            # set the betting strategy object as in the beginning
            betStrategy.__init__(**initial_state)
            
        return outcomes, bankruptcy, max_consecutive_loses