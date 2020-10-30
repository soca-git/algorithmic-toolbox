
def max_pairwise_product(numbers):
    max1 = 0
    max2 = 0
    for number in numbers:
        if number >= max1:
            max2 = max1
            max1 = number

        elif number > max2:
            max2 = number 

    return max1 * max2



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
