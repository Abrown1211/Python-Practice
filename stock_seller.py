class StockHolding:
    
    def __init__( self, symbol, totalShares, initialPrice ):
        self.symbol = symbol
        self.totalShares = totalShares
        self.initialPrice = initialPrice
        
    def getSymbol(self):
        return self.symbol
    
    def getNumShares(self):
        return self.totalShares
    
    def getInitialPrice(self):
        return self.initialPrice
    
    def sellShares(self, sharesToSell ):
        self.sharesToSell = sharesToSell   #method to sell shares from the clients stockholdings, throws error if stockholding shares are exceeded. 
        if self.totalShares - sharesToSell >= 0:
            self.totalShares = self.totalShares - sharesToSell
            print("Your total remaining shares are: {}".format( self.totalShares ))
        else:
            raise ValueError("You do not have that many shares to sell.")
        return self.totalShares, sharesToSell
        
    #method to determine if a profit exists and output the result.
    def estimatedProfit(self, finalPrice, sharesToSell):
        estimatedProfit = (finalPrice - self.initialPrice) * sharesToSell
        if estimatedProfit > 0:
            print("Estimated profit for selling {0} {1} shares is {2}".format( sharesToSell, self.symbol, estimatedProfit ))
        else:
            print("This trade is not profitable")
        return estimatedProfit
                          
        
def getInputs():
    symbol = input("Enter the symbol for the stock you wish to sell: ")
    totalShares = int(input("How many Shares of this stock do you have?: "))
    initialPrice = float(input("Initial share price (in dollars) : "))
    finalPrice = float(input("What is the final share price (in dollars) : "))
    sharesToSell = float(input("How many shares would you like to sell?: "))
    return symbol, totalShares, initialPrice, finalPrice, sharesToSell


def main():
    symbol,totalShares, initialPrice, finalPrice, sharesToSell = getInputs()
    sh = StockHolding( symbol, totalShares, initialPrice )
    sh.sellShares( sharesToSell )
    sh.estimatedProfit( finalPrice, sharesToSell)

main()
    