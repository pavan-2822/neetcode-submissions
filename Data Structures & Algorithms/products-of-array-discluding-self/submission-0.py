class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        k=[1]*n

        left_p=1
        for i in range(n):
            k[i]=left_p
            left_p *=nums[i]

        right_p=1
        for j in range (n-1,-1,-1):
            k[j]*=right_p
            right_p *= nums[j]

        return k
