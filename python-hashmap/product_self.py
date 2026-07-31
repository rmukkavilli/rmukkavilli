def prodcut_self(nums: list[int]| None)  -> list[int]:
    if not nums:
        return []
    res = [1] * len(nums)
    lp = 1
    for i in range(len(nums)):
        res[i] = lp
        lp *=nums[i]

    rp = 1
    for i in range(len(nums) -1, -1, -1):
        res[i] *= rp
        rp *=nums[i]
    return res

nums = [1,2,3,4]
print(prodcut_self(nums))

# unit test cases
def test_empty_nums():
    assert prodcut_self([]) == []

def test_nums_None():
    assert product_selt(None) == []

def tst_nums_single():
    assert product_self([1]) == [1] 