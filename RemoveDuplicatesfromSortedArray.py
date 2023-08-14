class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #cast and sort nums into a set (no duplicates allowed) and replace nums in-place by using [:]
        nums[:] = sorted(set(nums))
        return len(nums)

        #good alternative with loops below
        #j = 0
        #for i in range(1, len(nums)):
        #   if nums[j] != nums[i]:
        #       j += 1
        #       nums[j] = nums[i]
        #return j + 1