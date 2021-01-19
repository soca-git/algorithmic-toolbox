# Uses python3
import sys


def optimal_summands(n):
    prizes = []
    i = 1
    while not n == 0:
        r = n - i
        if r < 0:
            prizes.append(i)
            prizes.pop(prizes.index(r*-1))
            n = 0
        elif r not in prizes:
            prizes.append(i)
            n = r
        i += 1

    return prizes



def fast_optimal_summands(n):
    prizes = []
    i = 1
    csum = 0
    while not csum == n:
        csum += i
        prizes.append(i)
        if csum > n:
            prizes.pop(prizes.index(csum-n))
            csum = n
        i += 1

    return prizes



if __name__ == '__main__':
    input = sys.stdin.read()
    #input = '1000000000'
    n = int(input)
    summands = fast_optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
