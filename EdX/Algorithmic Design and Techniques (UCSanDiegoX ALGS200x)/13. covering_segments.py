# Uses python3

import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    # Sort segments by their end points
    segments.sort(key=lambda s: s.end)
    
    points = []
    current_point = None
    
    for segment in segments:
        if current_point is None or current_point < segment.start:
            current_point = segment.end
            points.append(current_point)
    
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for point in points:
        print(point, end=' ')