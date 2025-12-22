import sys

def main():
    data = sys.stdin.readlines()
    N = len(data)
    pts = []
    for line in data:
        line = line.split(",")
        pt = [int(x) for x in line]
        pts.append(pt)
    
    res = 0
    for i in range(N):
        for j in range(i + 1, N):
            pt1, pt2 = pts[i], pts[j]
            res = max(res, (abs(pt1[0]-pt2[0])+1)*(abs(pt1[1]-pt2[1])+1))
    print(res)


if __name__ == "__main__":
    main()