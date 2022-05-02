

 # Using the least amount of coins using American coin system, make n cents

 # coins = [1, 5, 10, 25] Normal minted coins in every day use

from threading import local

from pyparsing import makeHTMLTags


coins = [1,5,10,25]

def makeChange(n):

    minCoins = 0

    for i in reversed(range(0,len(coins))):
    
        if n == 0:
            return minCoins
        
        if coins[i] <= n:
            tempCount = n//coins[i]
            minCoins += tempCount
            n = n - (tempCount*coins[i])

    return minCoins
    
print(makeChange(1))
#     return minCoins