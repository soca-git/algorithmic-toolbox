# Uses python3
import math

def get_change(m):
    if m < 1 or m > 1000:
        #print('Error: m not within accepted range (1 <= m <= 1000).')
        return None

    ncoins = 0
    coins = [10, 5, 1]
    for coin in coins:
        if coin > m:
            continue

        ncoin = math.floor(m/coin)
        ncoins += ncoin
        m -= ncoin * coin

    return ncoins



if __name__ == '__main__':
    #print('Please enter value to be converted to change:')
    m = int(input())
    print(get_change(m))
