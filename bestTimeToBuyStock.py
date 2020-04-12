def bestTimeToBuyStock(prices):
    j = 1
    sum = 0
    for i in range(len(prices)-1):
        if prices[j]-prices[i] > 0:
            sum += prices[j] - prices[i]
        j = j + 1
    return sum


prices = [7,1,5,3,6,4]
print(bestTimeToBuyStock(prices))