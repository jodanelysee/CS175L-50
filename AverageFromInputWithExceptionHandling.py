def main():
    count = 0
    num = 0
    amount = 0

    try:
        numbers_file = open('numbers.txt', 'r')
    except IOError:
        print('An error has occured trying to read the file')

    for line in numbers_file:
        try:
            #numbers_file = open('numbers.txt', 'r')
       
            #for line in numbers_file:
            #count = count + 1
            num = float(line)
            count = count + 1
            amount = amount + num
            print('I read in',count,'number(s)\tCurrent number is: ',f'{num:.2f}', 'Total  is:',amount)

        except ValueError:
            print('An error has occured because there was non-numeric data found')
            
    average = (amount)/(count)
    print('Average: ',average)
            
    numbers_file.close()

        #except IOError:
            #print('An error has occured trying to read the file')

        #except ValueError:
            #print('An error has occured because there was non-numeric data found')

if __name__ == '__main__':
        main()
