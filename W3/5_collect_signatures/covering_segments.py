# Uses python3
import sys
from collections import namedtuple

# named tuples are lightweight objects
# segment.start, segment.end
Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    visits = []
    segments = sorted(segments, key=lambda x:x.end, reverse=False)
    for segment in segments:
        if not visits or segment.start > visits[-1]:
            visits.append(segment.end)

    return visits

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = '3 1 3 2 5 3 6'
    #input = '5 1 4 7 10 10 13 14 16 3 6'
    #input = '4 4 7 1 3 2 5 5 6'
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
