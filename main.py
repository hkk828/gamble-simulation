import random
from strategy.martingale import martingale
from utils.plot import betplot
from utils.simulation import monteCarlo
from collections import Counter
from sys import maxsize


if __name__ == '__main__':
    # parameters for the martingale strategy
    n_trial = 100
    win_prob = 18 / 37
    asset = 1024
    default_bet = 1
    ratio = 2

    # parameters for the simulation
    seed = random.randrange(maxsize)    # generate random seed from 0 ~ sys.maxsize-1
    random.seed(seed)                   # set the random seed for the reproducibility
    n_sim = 100

    # create betting strategy object
    betStrategy = martingale(win_prob=win_prob, asset=asset, default_bet=default_bet, ratio=ratio)
    
    # get the monte carlo simulation results
    outcomes, bankruptcy, max_consecutive_loses = monteCarlo.run(
                                                        n_sim=n_sim, betStrategy=betStrategy, n_trial=n_trial, seed=seed,
                                                        save=True, dpi=300, show=False)

    # number of bankruptcy in the simulation
    print(f'Bankrupt {len(bankruptcy)} times out of {n_sim} simulations ({len(bankruptcy)/n_sim*100} %)')

    # average final asset
    avg_asset = sum(outcomes) / len(outcomes)
    print(f'Average final asset after {n_trial} betting: {avg_asset:.2f}')

    # average final asset when bankrupt if any
    bankrupt_sum = 0
    for sim in bankruptcy:
        bankrupt_sum += outcomes[sim]

    # average final asset when not bankrupt
    nonBankrupt_sum = avg_asset * len(outcomes) - bankrupt_sum 

    print(f'Average final asset when not bankrupt: {nonBankrupt_sum / (len(outcomes) - len(bankruptcy)):.2f}')    
    if bankruptcy:
        print(f'Average final asset when bankrupt: {bankrupt_sum / len(bankruptcy):.2f}')

    # distribution of max_consecutive_lose during the simulation
    lose_dist = Counter(max_consecutive_loses)
    betplot.barChart(x=lose_dist.keys(),
                     y=lose_dist.values(),
                     save=True,
                     dpi=200,
                     path=f'imgs/{type(betStrategy).__name__}/{seed}_fullDist.png',
                     show=True)

    # distribution of max_consecutive_lose when not bankrupt (only executed if there was at least one bankruptcy)
    if bankruptcy:
        lose_dist.pop(10)    # bankrupt only if lost 10 times
        betplot.barChart(x=lose_dist.keys(),
                        y=lose_dist.values(),
                        save=True,
                        dpi=200,
                        path=f'imgs/{type(betStrategy).__name__}/{seed}_nonBankruptDist.png',
                        show=True)