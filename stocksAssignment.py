#CS175L-50
#Jodan Elysee
#Stocks Assignment

COMISSION_RATE = 0.03
numberOfShares = float(input('Joe, how many shares would you like to buy?'))
priceOfShare = float(input('What is the price for one share?'))
priceOfTotalShares = numberOfShares * priceOfShare
addComission = priceOfTotalShares * COMISSION_RATE
total = priceOfTotalShares + addComission
float(total)
print('You paid: $', priceOfTotalShares, 'for the shares')
print('You paid: $', addComission, 'for the comission')
print('You paid in total: $', total)
numberOfShares2 = float(input('How many shares would you like to sell?'))
priceOfShare2 = float(input('How much will you sell for a single share?'))
priceOfTotalShares2 = numberOfShares2 * priceOfShare2
addComission2 = priceOfTotalShares2 * COMISSION_RATE
total2 = priceOfTotalShares2 + addComission2
float(total2)
print('You sold the stock for: $', priceOfTotalShares2)
print('You paid : $', addComission2, 'for the comission when your broker bough the shares back')
priceAfterComission = priceOfTotalShares2 - addComission2
profit = priceAfterComission - total
float(priceAfterComission)
print('Your profit will be: $',profit)
                        
