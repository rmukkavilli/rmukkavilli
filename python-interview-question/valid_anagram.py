
def valid_angram(s,t):
    if len(s) != len(t):
        return False
    dict1 ={}
    dict2 = {}
    for ch in s:
            dict1[ch] = dict1.get(ch, 0)+1
    for ch in t:
            dict2[ch] = dict2.get(ch, 0)+1
    return dict1 == dict2






s = "listen"
t = "silent"
print(valid_angram(s,t))
