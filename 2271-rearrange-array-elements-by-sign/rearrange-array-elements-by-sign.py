class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0]*n
        posPointer = 0
        negPointer = 1
        for i in range(0,n):
            if nums[i] > 0:
                result[posPointer] = nums[i]
                posPointer += 2
            else:
                result[negPointer] = nums[i]
                negPointer += 2

        return result
        