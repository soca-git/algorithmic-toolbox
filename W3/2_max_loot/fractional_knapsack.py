# Uses python3
import sys



class Item:

    def __init__(self, w, v):
        self.weight = w
        self.value = v
        self.unitvalue = v/w

    def details(self):
        print(self.weight, self.value)



def get_optimal_value(capacity, weights, values):
    value = 0.
    items = []
    for i in range(0, len(weights)):
        items.append(Item(weights[i], values[i]))

    items = sorted(items, key=lambda x:x.unitvalue, reverse=True)
    
    for item in items:
        #item.details()
        if item.weight <= capacity:
            capacity -= item.weight
            value += item.value
        else:
            return value + item.unitvalue * capacity
        
    return value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    #data = list(map(int, '3 50 60 20 100 50 120 30'.split()))
    #data = list(map(int, '1 1000 500 30'.split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
