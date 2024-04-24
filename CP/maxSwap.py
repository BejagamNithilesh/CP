class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(x) for x in str(num)]
        lastIndex = {val: i for i, val in enumerate(nums)}

        for i in range(len(nums)):
            for d in range(9, nums[i], -1) :
                if d in lastIndex and lastIndex[d] > i:
                    nums[i], nums[lastIndex[d]] = nums[lastIndex[d]], nums[i]
                    return int("".join(map(str,nums)))
        return num