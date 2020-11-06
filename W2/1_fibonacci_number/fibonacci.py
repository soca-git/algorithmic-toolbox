
# recursive method (slow)
def fibonacci_recursive(n):
    if (n <= 1):
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)



# loop method (fast)
def fibonacci_loop(n):
    if (n <= 1):
        return n

    fnumbers = [0, 1]
    for i in range(2, n+1):
        fnumbers.append(fnumbers[i-1] + fnumbers[i-2])

    return fnumbers[-1]



############
### MAIN ###
############

if __name__ == "__main__":
    n = int(input())
    print(fibonacci_loop(n))
