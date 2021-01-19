# python3
import sys


def compute_min_refills(distance, tank, stops):
    stops.reverse()
    tankrange = tank # starting range of tank
    index = 0 # stop index
    nstops = 0 # stop counter
    cstop = None # current stop
    
    # first check if the initial range is enough to reach the second city.
    if tankrange >= distance:
        return nstops

    # while checking stops further away from the current stop
    while not stops[index] == cstop:
        if stops[index] <= tankrange:
            # update range of tank (refuel)
            tankrange = stops[index] + tank
            # update the number of stops
            nstops += 1
            # update the current stop
            cstop = stops[index]
            #print('Refueling at ... %s (stop %s). New range is %s.' % (stops[index], nstops, tankrange))
            index = 0
            # check if the updated range is enough to reach the second city.
            if tankrange >= distance:
                return nstops
        else:
            index += 1

    # if the range is never greater than the journey distance,
    # we will return to the current stop in the journey.
    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    #d, m, _, *stops = map(int, '950 400 4 200 375 550 750'.split())
    #d, m, _, *stops = map(int, '500 200 4 100 200 300 400'.split())
    #d, m, _, *stops = map(int, '1000 250 5 100 250 400 650 750 1000'.split())
    #d, m, _, *stops = map(int, '10 3 4 1 2 5 9'.split())
    #d, m, _, *stops = map(int, '10 11 4 1 2 5 9'.split())
    print(compute_min_refills(d, m, stops))
