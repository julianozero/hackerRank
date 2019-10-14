def countSwaps(a):
    swaps = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps+=1
    return swaps

def result(swaps, firstElement, lastElement):
    print("Array is sorted in %d swaps." %swaps)
    print("First Element: %d" %firstElement)
    print("Last Element: %d" %lastElement)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    result(countSwaps(a), a[0], a[n-1])