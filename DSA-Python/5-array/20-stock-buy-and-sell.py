# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



# brute force - O(n²), O(1)
def stock_buy_and_sell_1(prices:list[int]) -> int:
    n, diff = len(prices), 0
    
    for i in range(n):
        low = prices[i]
        high = prices[i]
        
        for j in range(i+1, n):
            if prices[j] > high:
                high = prices[j]
                
        diff = max(diff, high-low)
            
    return diff



# two pointer
def stock_buy_and_sell_2(prices:list[int]) -> int:
    min_price, profit = float('inf'), 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = max(profit, price - min_price)
            
    return profit



if __name__ == "__main__":
    loop = int(input())
    
    for i in range(loop):
        prices = list(map(int, input().split()))
        
        res = stock_buy_and_sell_1(prices)
        
        # res = stock_buy_and_sell_2(prices)
        
        print(res)
        
        
'''
5
7 1 5 3 6 4
7 6 4 3 1
5
2 1 2 0 1
-2 -3
'''