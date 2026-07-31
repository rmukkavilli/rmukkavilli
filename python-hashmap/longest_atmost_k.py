# O(N) Time and O(1) is space complexity

def longest_section_with_k_failures(
    statuses: list[str],
    k: int
) -> int:
    left = 0
    count = 0
    max_count = 0
    for right in range(len(statuses)):
        if statuses[right] == 'FAIL':
            count +=1
        while(count > k):
            if statuses[left] == 'FAIL':
                count -=1
            left +=1
    max_count = max(max_count, right - left +1)
    return max_count

        



statuses = ["PASS", "FAIL", "PASS", "PASS", "FAIL", "PASS", "PASS"]
k = 1
print(longest_section_with_k_failures(statuses, k))