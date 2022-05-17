

 # Using the least amount of coins using American Denominations, make n cents

 # coins = [1, 5, 10, 25] Normal minted coins in every day use

#Hard set since tit's only the American system
#Time Complexity: O(n) one pass through the coin array, technically since it's just for it can be considerd O(1)
#Space Complexity: O(1) since no new space is created other than to hold one value therefore O(1)

coins = [1,5,10,25]

def makeChange(n):

    minCoins = 0

    for i in reversed(range(0,len(coins))):
    
        if n == 0:
            return minCoins
        
        # start from largest # and find the max amount needed
        if coins[i] <= n:
            tempCount = n//coins[i]
            minCoins += tempCount
            n = n - (tempCount*coins[i])

    return minCoins
    
print(makeChange(1))
#     return minCoins