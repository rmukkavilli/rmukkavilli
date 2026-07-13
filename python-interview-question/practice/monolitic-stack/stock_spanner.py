# This is LeetCode 901 — Online Stock Span.
# TIme O(n)
# Space O(n) where as next using O(1)


class StockSpanner:

    def __init__(self):
        self.stock_stack = []

    def next(self, price: int) -> int:
        current_span = 1
        while self.stock_stack and price >= self.stock_stack[-1][0]:
            item = self.stock_stack.pop()
            current_span = current_span + item[1]
        self.stock_stack.append((price, current_span))
        return current_span


stock = StockSpanner()

print(stock.next(100))  # 1
print(stock.next(80))   # 1
print(stock.next(60))   # 1
print(stock.next(70))   # 2
print(stock.next(60))   # 1
print(stock.next(75))   # 4
print(stock.next(85))   # 6