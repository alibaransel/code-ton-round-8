arr = []
last = 0
lastI = 0
#currRes = 0
#cri = 0

def addSorted(k):
    for i in range(len(arr)):
        if k < arr[i]:
            arr.insert(i, k)
            if k < last:
                lastI += 1
            else:

            return
    arr.append(k)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(s) for s in input().split(" ")]
        res = []
        for j in range(len(a)):
            addSorted(a[j])
            res.append(last )



