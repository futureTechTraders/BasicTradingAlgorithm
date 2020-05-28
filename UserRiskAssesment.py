import numpy as np  


accountSize = float(input('What is the size of your account?: '))
accountRisk = input('What is your account risk, please enter as a %: ')
targetPrice = float(input('What is your target price?: '))
entryPrice = float(input('Entry Price?: '))
stopLoss = float(input('What is your stop loss level(price)?: '))

class UserRiskAssesment:
    def positionLevels():
        profitPerShare = targetPrice - entryPrice
        lossPerShare = entryPrice - stopLoss
        ReturnRiskRatio = profitPerShare/lossPerShare #This number should be atleast 2 for a good trade
        maxLoss = ((float(accountRisk.rstrip('%')))/100) * accountSize
        numShares = int(maxLoss/lossPerShare)
        positionValue = entryPrice * numShares
        maxProfit = np.round((profitPerShare * numShares),2)

        print('Your maximum loss given your account size and risk, is: $' + str(maxLoss))
        print('Given your stop loss and maximum loss potential, you should purchase at max ' + str(numShares) + ' shares')
        print('Given your target price, your max profit is: $' + str(maxProfit))


    positionLevels()
