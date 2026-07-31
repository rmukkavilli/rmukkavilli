#@ Starting from today and moving backward, how many consecutive days had prices less than or equal to today’s price?
# Amortized time per call: O(1)
# Worst case for one call: O(n)
# Total time for n calls: O(n)
# Space: O(n)
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span =1
        while self.stack and price >= self.stack[-1][1]:
            print(price)
            prev_span, prev_stock = self.stack.pop()
            print("prev_span", prev_span, "prev_price", prev_stock)
            span +=prev_span
            print("span" , span)
        self.stack.append([span, price])
        return span
    


stock = StockSpanner()

print(stock.next(100))  # 1
print(stock.next(80))   # 1
print(stock.next(60))   # 1
print(stock.next(70))   # 2
print(stock.next(60))   # 1
print(stock.next(75))   # 4
print(stock.next(85))   # 6



