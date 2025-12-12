import sys
import heapq 

class DSU:
    def __init__(self, size: int) -> None:
        self.parents = [i for i in range(size)]
        self.sizes = [1 for _ in range(size)]

    def find(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def unite(self, x: int, y: int) -> bool:
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        if self.sizes[x_root] < self.sizes[y_root]:
            x_root, y_root = y_root, x_root
        self.parents[y_root] = x_root
        self.sizes[x_root] += self.sizes[y_root]
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def main():
    data = sys.stdin.readlines(); 
    idx_to_pt, pt_to_idx = dict(), dict()

    for idx, line in enumerate(data):
        line = line.split(",")
        x, y, z = [int(x) for x in line]
        idx_to_pt[idx] = (x, y, z)
        pt_to_idx[(x, y, z)] = idx
    N = len(data)
    dsu = DSU(len(data)+20)

    dists = [] 

    for i in range(N):
        for j in range(i + 1, N):
            pt1 = idx_to_pt[i]
            pt2 = idx_to_pt[j]
            dist = (pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2+(pt1[2]-pt2[2])**2
            heapq.heappush(dists, (dist, (i, j)))

    cnt = 0
    while True:
        dist, pts = heapq.heappop(dists)
        dsu.unite(pts[0], pts[1])
        print(idx_to_pt[pts[0]], idx_to_pt[pts[1]])
        f = dsu.find(pts[0])
        if dsu.sizes[f] == N:
            print(idx_to_pt[pts[0]][0]*idx_to_pt[pts[1]][0])
            break

if __name__ == "__main__":
    main()