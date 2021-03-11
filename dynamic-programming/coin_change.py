# minimum number of coins needed given int[] coins and amount 

def minimum_coin(coins, amount):
  dp = [float("inf")] * (amount + 1)
  dp[0] = 0
  
  for i in range(1, amount + 1):
    for coin in coins:
      if i >= coin:
        dp[i] = min(dp[i], dp[i - coin] + 1)
  
  return -1 if dp[-1] >= float("inf") else dp[-1]

minimum_coin([1,3,5], 11)
