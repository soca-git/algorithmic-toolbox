
import math

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



############
### MAIN ###
############

if __name__ == "__main__":
    input = '2 3 9 2 2'
    alist = list(map(int, input.split()))
    print(merge_sort(alist))
