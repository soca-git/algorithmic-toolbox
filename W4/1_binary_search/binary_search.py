# Uses python3
import sys
import math

def binary_search(a, x, l, r):
    #print(a, x, l, r)
    if r >= l:
        m = l + ((r - l) // 2)

        if x == a[m]:
            return m

        if x < a[m]:
            return binary_search(a, x, l, m-1)
        elif x > a[m]:
            return binary_search(a, x, m+1, r)

    else:
        return -1



def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1



if __name__ == '__main__':
    input = sys.stdin.read()
    #input = '6 1 5 8 12 13 15 6 8 1 23 1 11 15'
    #input = '5 1 5 8 12 13 1 23'
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x, 0, len(a)-1), end = ' ')
        #binary_search(a, x, 0, len(a)-1)
