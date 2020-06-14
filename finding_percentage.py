if __name__ == "__main__":
    n = int(input())
    s = dict()
    for i in range(n):
        name, p, c, m = input().split(" ")
        a = (float(p) + float(c) + float(m)) / 3
        s[name] = a
    print(f"{s[input()]:.2f}")
