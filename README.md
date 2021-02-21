# Gamble Betting Strategy Simulation

## [Martingale](https://en.wikipedia.org/wiki/Martingale_(betting_system))

Martingale is a betting strategy that was popular around 18th century France.  
The most general setting of the strategy would be as follows.  
A gambler plays a game that has a postive probability of winning, and starts betting with a default bet (or stake).  
If a gambler wins, bet again with the same amount, but if a gambler loses, double the bet.  
Martingale is usually applied to roulette where the probability of getting even/odd, or black/red is close to 0.5.

**Advantage**  
Despite its simplicity, the strategy almost surely wins the money. Consecutive loses make the loss grows exponentially, but any single win at the end recovers all the loss and adds extra default bet.  

**Disadvantage**  
Theoretically, one can never lose money with the martingale strategy. However, no gambler has infinite amount of money, which can lead to bankruptcy in a finite number of games. Furthermore, some casinos restrict the maximum bet so that a gambler cannot double one's bet after some consecutive loses.  

## Contents
In this repository, I shared codes to implement monte carlo simulation for martingale strategy.  
```simulation``` module in ```utils``` directory can take any other strategy that conforms the structure of ```martingale``` class in ```strategy.martingale```. Therefore, one can simulate one's own strategy with some adjustments.  

If you want to run any module on its own not through ```main.py```, do the followoing.  
Type the following line on command line in the root directory where the ```main.py``` is stored.
```bash
pip install -e .
```
or
```bash
python3.x -m pip install -e .
```
with x replaced by the python version you use.

**Parameters for the martingale strategy**  
```main.py``` creates the martinagle class object with  
  number of bets = 100  
  probability of winning = 18 / 37 (--> when bet on parity, or color in roulette)  
  starting asset = 1024  
  default bet = 1  
  multiplication factor when losing the bet = 2  

**Parameters for the simulation**  
  number of simulations = 100
  random seed = 5721682456115269080  
  
## Result
Bankrupt 3 times out of 100 simulations.  
Average final asset: 1038.74  
Average final asset conditioned on not bankrupt: 1069.91  
Average final asset conditioned on bankrupt: 31.00  

**3 (random) result plots from 100 simulations**  
<img src="https://raw.githubusercontent.com/hkk828/gamble-simulation/master/imgs/martingale/5721682456115269080_0.png" width=60% height=60%>  
<img src="https://raw.githubusercontent.com/hkk828/gamble-simulation/master/imgs/martingale/5721682456115269080_2.png" width=60% height=60%>  
<img src="https://raw.githubusercontent.com/hkk828/gamble-simulation/master/imgs/martingale/5721682456115269080_21.png" width=60% height=60%>  

**Distribution of consecutive loses**  
<img src="https://raw.githubusercontent.com/hkk828/gamble-simulation/master/imgs/martingale/5721682456115269080_fullDist.png" width=60% height=60%>  
**Only when not bankrupt**  
<img src="https://raw.githubusercontent.com/hkk828/gamble-simulation/master/imgs/martingale/5721682456115269080_nonBankruptDist.png" width=60% height=60%>
