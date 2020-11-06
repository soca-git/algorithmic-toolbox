
import sys

# given method
def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b



# my method
def lcm(a, b):
    smaller, larger = min(a, b), max(a, b)
    lcm = larger
    while True:
        if lcm % smaller == 0:
            return lcm
        lcm = lcm + larger



if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

