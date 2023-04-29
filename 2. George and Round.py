def George_and_Round(n,m):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    i = 0
    while i < len(a):
        j = 0
        while j < len(b):
            if a[i] <= b[j]:
                del(a[i])
                i-=1
                break
            j+=1
        i+=1
    print(a)
    print(len(a))
n, m = map(int, input().split())
George_and_Round(n,m)
