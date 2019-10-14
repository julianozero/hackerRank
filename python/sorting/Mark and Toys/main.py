import os

# Complete the maximumToys function below.
def maximumToys(prices, k):
    maximum = 0
    prices.sort()
    
    for price in prices:
        if k <= 0 or k < price:
            break
        k -= price
        maximum += 1
    
    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    fptr.write(str(result) + '\n')
    fptr.close()