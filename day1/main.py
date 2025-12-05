import sys

def main():
    A = sys.stdin.readlines()
    start = 50
    res = 0
    for line in A:
        line = line.strip()
        direction, value = line[0], int(line[1:])
        if value >= 100:
            res += value//100
        value %= 100 
        prev_start = start
        check = False
        if direction == 'L':
            start -= value
            start %= 100
            if start > prev_start and prev_start != 0:
                check = True
        else:
            start += value
            start %= 100
            if start < prev_start and prev_start != 0:
                check = True
        if start == 0:
            res += 1
        elif check:
            res += 1
    print(res)     

if __name__ == "__main__":
    main()