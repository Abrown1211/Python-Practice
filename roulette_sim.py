from random import randint

#Global Variable
roulleteList = ['00','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22',
              '23','24','25','26','27','28','29','30','31','32','33','34','35','36']


def welcome():
    #Starting Message
    amount = input('Enter the number of dollars you start with: ')
    turns = input('Enter the number of turns you will play: ')
    bidAmount = input('Enter how many dollars you will bet for each spin: ')
    return amount, turns,bidAmount


def gameselection():
    #Strategy Selection options
    print('Choose one of the following strategy choices')
    print('    -Bet on a (s)ingle number (pays 35 to 1)')
    print('    -Bet on (e)ven or odd numbers (pays 1 to 1)')
    print('    -Bet on a (d)ozen numbers (pays 2 to 1)')
    options = input('Enter your strategy (s, e, d): ')
    return options


def optionsgame(options):
    if options =='s':
        return input('Enter the single number you want to bet on (00 or 0 to 36): ')
    elif options == 'e':
        return input('Enter 1 to bet on odd numbers, 2 for even numbers: ')
    elif options == 'd':
        return input('Enter 1 to bet on numbers 1-12, 2 for numbers 13-24, or 3 for numbers 25-36: ')


#Function to calculate the output in case of singlenum options
def singlenum(amount,turns,bidAmount,numberSelection):
    amount = int(amount)
    startPrice = amount
    turns = int(turns)
    bidAmount = int(bidAmount)
    rounds = 0
    wins = 0
    while amount >= bidAmount and rounds < turns:
        amount = amount - bidAmount
        rounds = rounds + 1
        if roulleteList[randint(0,37)] == numberSelection:
            amount = amount + 35*bidAmount
            wins = wins + 1
    return rounds, wins, amount, startPrice


#Function to calculate the output in case of even or odd options
def evenodd(amount,turns,bidAmount,numberSelection):
    amount = int(amount)
    startPrice = amount
    turns = int(turns)
    bidAmount = int(bidAmount)
    rounds = 0
    wins = 0
    while amount >= bidAmount and rounds < turns:
        amount = amount - bidAmount
        rounds = rounds + 1
        r = randint(0,37)
        if r % 2 == 0 and r != 0:
            if numberSelection == '1':
                amount = amount + 2*bidAmount
                wins = wins + 1
        else:
            if numberSelection == '0':
                amount = amount + 2*bidAmount
                wins = wins + 1
    return rounds, wins, amount, startPrice


def dozen(amount,turns,bidAmount,numberSelection):
    amount = int(amount)
    startPrice = amount
    turns = int(turns)
    bidAmount = int(bidAmount)
    rounds = 0
    wins = 0
    while amount >= bidAmount and rounds < turns:
        amount = amount - bidAmount
        rounds = rounds + 1
        r = randint(0,37)
        if r >= 2 and r <= 13:
            if numberSelection == '1':
                amount = amount + 3*bidAmount
                wins = wins + 1
        elif r>=14 and r<=25:
            if numberSelection == '2':
                amount = amount + 3*bidAmount
                wins = wins + 1
        elif r>=26 and r<=37:
            if numberSelection == '3':
                amount = amount + 3*bidAmount
                wins = wins + 1
    return rounds, wins, amount, startPrice
    


def winnings(rounds, wins, amount, startPrice):
    print('After ' + str(rounds) + ' turns')
    print('Wins: ' + str(wins) + ' ('+str(float(100*float(wins)/float(rounds))) + '%)')
    print('Losses: ' + str(rounds-wins) + ' (' + str(100-(100*float(wins)/float(rounds))) +'%)')
    print('Ending bank: ' + str(amount))
    print('Net winnings: $' + str(amount - startPrice))
    return


def gamerun(options,amount,turns,bidAmount,numberSelection):
    if options =='s':
        rounds, wins, amounts, startPrice = singlenum(amount,turns,bidAmount,numberSelection)
    elif options == 'e':
        rounds, wins, amounts, startPrice = evenodd(amount,turns,bidAmount,numberSelection)
    elif options == 'd':
        rounds, wins, amounts, startPrice = dozen(amount,turns,bidAmount,numberSelection)
    return rounds, wins, amounts, startPrice

def main():
    amount, turns, bidAmount = welcome()
    options = gameselection()
    numberSelection = optionsgame(options)
    rounds, wins, amounts, startPrice = gamerun(options,amount,turns,bidAmount,numberSelection)
    winnings(rounds, wins, amounts, startPrice)
    
main()
