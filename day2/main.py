import sys

def main():
    intervals = sys.stdin.readlines()[0].split(",")
    A = []
    for i, v in enumerate(intervals):
        vv = [int(x) for x in v.split("-")]
        A.append(vv)

    res = 0
    for interval in A:
        l, r = interval[0], interval[1]
        for v in range(l, r+1):
            v_str = str(v)
            len_v = len(v_str)
            for i in range(0, len_v//2 + 1):
                pref = v_str[:i+1]
                if len_v % (i + 1) == 0:
                    k = len_v // (i+1)
                    if k >= 2 and pref*k == v_str:
                        print(v)
                        res += v
                        break


    print(res)

if __name__ == "__main__":
    main()