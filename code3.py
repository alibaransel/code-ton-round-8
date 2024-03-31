if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        sArr = input().split(" ")
        n = int(sArr[0])
        k = int(sArr[1])

        if k == n:
            s = "1" + " 1" * (n-1)
            print(s)
        elif k == 1:
            s = "1"
            for x in range(n-1):
                s += " " + str(x+2)
            print(s)
        else:
            print(-1)
