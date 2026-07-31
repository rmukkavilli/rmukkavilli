import heapq

def top_k_errors(errors: list[str], k: int) -> list[str]:
    # Write your solution here.
    error_dict = {}
    heap = []
    for error in errors:
        error_dict[error] = error_dict.get(error, 0)+1
    for error,frequency in error_dict.items():
        heapq.heappush(heap, (frequency, error))
        if len(heap) > k:
            heapq.heappop(heap)
    return [error for frequency, error in heap]


errors = [
    "timeout",
    "401",
    "timeout",
    "500",
    "401",
    "timeout"
]
k = 2
print(top_k_errors(errors,k))