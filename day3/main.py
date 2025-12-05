import sys
from typing import List, Tuple

def get_largest_valid_number(A: List[int], K: int) -> Tuple[str, int]:
    N = len(A)
    val = max(A[:N-K+1])
    idx = -1
    for i in range(0, N):
        if A[i] == val:
            idx = i
            break

    return (str(val), idx)

def main():
    batteries = sys.stdin.readlines()
    res = 0
    for line in batteries:
        line = line.strip()
        joltage_ratings = [int(x) for x in line]
        ret = ""
        for i in range(12, 0, -1):
            val, idx = get_largest_valid_number(joltage_ratings, i)
            joltage_ratings = joltage_ratings[idx+1:]
            ret += val
        res += int(ret)
    print(res)


if __name__ == "__main__":
    main()