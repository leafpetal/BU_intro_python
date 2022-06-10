#
# TT_security.py - Problem Set 6, Problem 4
#
# TT Securities    
#
# Computer Science 111
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Find the average price')
    print('(4) Find the min price and its day')
    print('(5) Find the max single-day change and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')

    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.

# function 3
def avg_price(prices):
    """ return the average price of 1 or more prices using loop.
        cannot use sum, min, or max functions
    """
    count = 0
    total_price = 0
    for i in range(len(prices)):
        count += 1
        total_price += prices[i]
    return total_price / count
#print(avg_price([10, 20, 18]))


# function 4
def min_day(prices):
    """
        takes a list of 1 or more prices and computes and 
        returns the day (i.e., the index) of the minimum price
    """
    min_index = 0
    for i in range(len(prices)):
        if prices[i-1] > prices[i]:
            min_index = i
    return min_index
#print(min_day([40,10,20,35,25]))


# function 5
def max_change_day(prices):
    """
        Take a list of 2 or more prices and computes and
        returns the day (i.e., the index) of the maximum 
        single-day change in price
    """
    diff_price = prices[1] - prices[0]
    max_day = 0
    for i in range(len(prices)-1):
        if prices[i+1] - prices[i] > diff_price:
            diff_price = prices[i+1] - prices[i]
            max_day = i+1
    return max_day
#print(max_change_day([10, 30, 20, 15, 50]))


# function 6
def any_above(prices, threshold):
    """
        Test if there is any value among prices that is above the threshold
    """
    count = 0
    for i in range(len(prices)):
        if prices[i] > threshold:
            count += 1
    if count > 0:
        return True
    else:
        return False
#print(any_above([20, 30, 15],12))


# function 7
def find_tts(prices):
    """
        Takes a list of 2 or more prices, and finds the best days on which to buy and sell the stock whose prices are given in the list of prices.
        Return the buy day, sell day, resulting profit
    """
    max_diff = prices[1] - prices[0]
    buy_day = 0
    sell_day = 1
    for i in range(len(prices)):
        for j in range(len(prices)):
            if prices[j] - prices[i] > max_diff:
                if j > i:
                    max_diff = prices[j] - prices[i]
                    buy_day = i
                    sell_day = j
    return [buy_day, sell_day, max_diff]
#print(find_tts([5, 10, 45, 35, 3]))
   

def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            average = avg_price(prices)
            print('The average price is', average)
        elif choice == 4:
            minimum = min_day(prices)
            print('The min price is', prices[minimum], 'on day', minimum)
        elif choice == 5:
            max_change = max_change_day(prices)
            print('The max single-day change occurs on day', max_change)
            print('when the price goes from', prices[max_change-1], 'to', prices[max_change])
        elif choice == 6:
            threshold = int(input('Enter the threshold: '))
            check_threshold = any_above(prices, threshold)
            if check_threshold == True:
                print('There is at least one price above', threshold)
            else:
                print('There are no prices above', threshold)
        elif choice == 7:
            tts_result = find_tts(prices)
            buy = tts_result[0]
            sell = tts_result[1]
            profit = tts_result[2]
            print('Buy on day', buy, 'at price', prices[buy])
            print('Sell on day', sell, 'at price', prices[sell])
            print('Total profit:', profit)
            
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
