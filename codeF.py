import math
from decimal import *

getcontext().prec = 1000

def f(t):
    if t == 1:
        return Decimal(a[1]).sqrt()
    return Decimal(f(t-1) + a[t]).sqrt()

if __name__ == "__main__":
    sArr = input().split(" ")
    n = int(sArr[0])
    q = int(sArr[1])
    a = [0] + [int(s) for s in input().split(" ")]
    for i in range(q):
        sArr = input().split(" ")
        k = int(sArr[0])
        x = int(sArr[1])
        a[k] = x
        print("-------" + str(math.floor(f(n))))

        
