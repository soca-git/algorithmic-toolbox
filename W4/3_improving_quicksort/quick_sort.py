# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    jl = l
    jr = jl
    #print(a)
    for i in range(l + 1, r + 1):
        #print(x, a[i])

        if a[i] < x:
            a[i], a[jl] = a[jl], a[i]
            jl += 1
        if a[i] == x:
            a[i], a[jr+1] = a[jr+1], a[i]
            jr += 1
            
        
        #print(a)
    return jl, jr


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return a
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #m = partition2(a, l, r)
    ml, mr = partition3(a, l, r)
    a = randomized_quick_sort(a, l, ml - 1);
    return randomized_quick_sort(a, mr + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    #input = '5 2 3 9 2 2'
    #input = '10 10 9 8 7 6 5 4 3 2 1'
    #input = '14 1 2 3 4 4 3 2 2 2 1 1 5 3 8'
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
