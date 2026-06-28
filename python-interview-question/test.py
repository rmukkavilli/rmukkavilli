def test_py(s):
    s.lower()
    print(s)
    for ch in s:
        if not ch.isalnum():
            print(ch)

s = "a man:::::::, a plan, a canal: pcnama"
nums = [[1,2,3],[2,3,4],[4,5,6]]
print(test_py(s))


# for row in nums:
#     print(row)
#     for col in row:
#         print(col)
        