import sys
from typing import List, Tuple

def main():
    data = sys.stdin.readlines()
    numbers = []
    ops = []
    for line in data:
        line = line[:-1]
        ret = []
        if line[0] not in "+*":
            for x in line:
                ret.append(x)
            numbers.append(ret)
        else:
            for x in line:
                if x:
                    ret.append(x)
            ops = ret 
    print(numbers)
    print(ops)
    res = 0
    curr = []
    op = ""
    print(numbers[0])
    print(numbers[1])
    print(numbers[2])

    for i in range(len(numbers[0])):
        ret = "" 
        for k in range(0, 4):
            ret += numbers[k][i]
        op += (ops[i] if ops[i] != " " else "")
        if ret.strip() == '':
            v = 0
            if op == "*":
                v = 1
                for x in curr:
                    v *= int(x)
                curr = []
            elif op == "+":
                for x in curr:
                    v += int(x)
                curr = []
            op = ""
            res += v
        else:
            curr.append(ret)
    print(res)



if __name__ == "__main__":
    main()