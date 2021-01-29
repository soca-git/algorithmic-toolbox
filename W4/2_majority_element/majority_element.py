# Uses python3
import sys
import math
#from merge_sort import merge_sort



def merge_sort(a):
    if len(a) == 1:
        return a

    m = math.floor(len(a)/2)

    al = merge_sort(a[:m])
    ar = merge_sort(a[m:])

    return merge(al, ar)



def merge(b, c):
    s = []
    while b and c:
        if b[0] <= c[0]:
            s.append(b[0])
            b.pop(0)
        else:
            s.append(c[0])
            c.pop(0)
    s = s + b + c
    return s



def get_majority_element_fast(a, left, right):
    # this checks if the array is size 0 or size 1
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    
    # algorithm
    majority = len(a)/2
    a = merge_sort(a) # O(nlogn)
    current_element = a[0]
    count = 0
    while len(a) > 0: # O(n)
        if a[0] == current_element:
            count += 1
            if count > majority:
                return a[0]
        else:
            count = 1
            current_element = a[0]
        #print(a[0], count)
        a.pop(0)

    return -1



def get_majority_element_naive(a, left, right):
    # this checks if the array is size 0 or size 1
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    
    # algorithm
    for i in a:
        current = i
        count = 0
        for j in a:
            if j == i:
                count += 1
        if count > len(a)/2:
            return i

    return -1



if __name__ == '__main__':
    input = sys.stdin.read()
    #input = '5 2 3 9 2 3 5 5 5 5 5 5'
    #input = '4 1 2 3 4'
    n, *a = list(map(int, input.split()))
    if get_majority_element_fast(a, 0, n) != -1:
        print(1)
    else:
        print(0)
