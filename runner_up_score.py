if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split(" ")))
    l.sort(reverse=True)
    m = max(l)
    i = 0
    for i in l:
        if i < m:
            break
    print(i)
