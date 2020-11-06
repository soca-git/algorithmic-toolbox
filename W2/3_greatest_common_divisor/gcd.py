import sys

# given method
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd



# my method
def gcd(a, b):
    smaller, larger = min(a, b), max(a, b)
    if smaller == 0:
        return larger
    else:
        return gcd(smaller, larger % smaller)





if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
