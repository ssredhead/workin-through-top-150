"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # #traverse the array (nums) and delete all instances of val
        # for n in nums:
        #     if n == val: 
        #         nums.remove(n)

        # #return the length of nums after all vals have been deleted
        # return len(nums)

        #solve in place with pythonic list comprehension
        #with nums[:] i.e. the whole list, it can be in place
        #O(n) time complexity and O(1) space complexity because it is in place
        nums[:] = [n for n in nums if n != val]
        return len(nums)