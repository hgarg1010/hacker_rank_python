import sys

if __name__ == "__main__":
    l = []
    n = int(input())
    for i in range(n):
        name = input()
        marks = float(input())
        l.append([name, marks])

    l.sort(key=lambda x: x[1])
    # print(l)
    m = l[0][1]
    mi = 1000
    nl = []
    for name, marks in l:
        if marks > m and marks <= mi:
            mi = marks
            nl.append(name)

    nl.sort()
    for i in nl:
        print(i)
