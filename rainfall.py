#CS175L-50
#Jodan Elysee
#Rainfall Quiz

totalRainfall = 0
average_monthly_rainfall = 0
numYears = int(input('How many years? '))
numMonths = 12
total = 0
#while numYears == 1
for year in range (1, numYears+1):
    print('For year: ', year)
    for month in range (1, numMonths+1):
        inches = float(input('Enter the rainfall amount for the month: '))
        total = total + inches
totalMonths = numMonths*numYears
average = total/totalMonths
print('For',totalMonths, 'months')
print(f'Total Rainfall: {total}')
print(f'Average Monthly Rainfall: {average: .2f} ')
