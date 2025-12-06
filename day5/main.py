import sys
from typing import List, Tuple

def main():
    data = sys.stdin.readlines()
    intervals, queries = [], []
    for line in data:
        line = line.strip()
        if line:
            if "-" in line:
                l, r = line.split("-")
                intervals.append((int(l), int(r)))
            else:
                queries.append(int(line))
    intervals = sorted(intervals, key=lambda x: x[1])
    new_intervals = []
    curr_interval = intervals[0]
    for i in range(1, len(intervals)):
        if curr_interval[1] < intervals[i][0]:
            new_intervals.append(curr_interval)
            curr_interval = intervals[i]
        else:
            curr_interval = (min(curr_interval[0], intervals[i][0]), max(curr_interval[1], intervals[i][1]))
    new_intervals.append(curr_interval) 
    res = 0
    for (l, r) in new_intervals:
        res += (r - l + 1)
    print(res)


if __name__ == "__main__":
    main()