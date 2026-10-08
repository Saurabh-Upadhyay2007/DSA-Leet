class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        sum = (n*(n+1))//2
        sum1 = 0
        for i in range(0,n):
             sum1 += nums[i]

        sum -= sum1

        return sum     