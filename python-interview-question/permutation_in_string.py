def permutation_in_string(s1, s2):
    window_size = len(s1)
    target = sorted(s1)
    # 8 -2 +1 = 7 
    for i in range(len(s2) - len(s1)+1):
        window = s2[i:i+window_size]
        if (sorted(window)) == target:
            return True
    return False

s1 = "adc"
s2 = "dcda"
print(permutation_in_string(s1, s2))