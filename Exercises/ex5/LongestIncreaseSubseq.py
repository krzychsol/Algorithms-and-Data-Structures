"""
Zadanie 3:
Na wykładzie podaliśmy algorytm działający w czasie O(n^2).
Proszę podać algorytm o złożoności O(nlog n).
"""
#O(nlogn)

def findidx(T,l,r,x):
    while r-l > 1:
        mid = l + (r-l)//2
        if T[mid] >= x:
            r = mid
        else:
            l = mid
    return r

def LIS(A):
    n = len(A)
    T = [0 for _ in range(n+1)]
    T[0] = A[0]
    length = 1

    for i in range(1,n):
        if A[i] < T[0]:
            T[0] = A[i]
        elif A[i] > T[length-1]:
            T[length] = A[i]
            length += 1
        else:
            T[findidx(T,-1,length-1,A[i])] = A[i]

    return length

##Wersja z wypisywaniem wyniku

def GetCeilIndex(arr, T, l, r, key):
    while r - l > 1:

        m = l + (r - l) // 2
        if arr[T[m]] >= key:
            r = m
        else:
            l = m

    return r

def LIS_v2(A):
    n = len(A)
    tailIdx = [0 for _ in range(n+1)]
    prevIdx = [-1 for i in range(n+1)]

    length = 1
    for i in range(1,n):
        if A[i] < A[tailIdx[0]]:
            tailIdx[0] = i
        elif A[i] > A[tailIdx[length-1]]:
            prevIdx[i] = tailIdx[length-1]
            tailIdx[length] = i
            length += 1
        else:
            pos = GetCeilIndex(A,tailIdx,-1,length-1,A[i])
            prevIdx[i] = tailIdx[pos-1]
            tailIdx[pos] = i

    i = tailIdx[length - 1]
    result = []
    while i >= 0:
        result.append(A[i])
        i = prevIdx[i]

    result.reverse()
    return result

A = [4, 10, 5, 1, 8, 2, 3, 4]
print(LIS_v2(A))