class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        find the majority element - the element that appears more than n/2 times
        assume the majority element always exists
        first try sorting the array

        This first approach works but is overly complicated and could actually just return nums[n//2]
        But it is also time and space complexity of O(nlogn) because of the sorting
        nums[:] = sorted(nums)
        majorityEl = 0
        changeIdx = 0
        for idx in range(len(nums)):
            if nums[idx] == majorityEl:
                pass
            else:
                changeIdx = idx
                break
        if changeIdx >= len(nums)/2:
            return nums[changeIdx]
        else:
            return nums[changeIdx - 1]

        Rather than employ a sorting algorithm or different data structure like a hashmap (which would allow you to 
        easily keep track of the occurances of a value), we can use the Moore Voting Algorithm
        If there is a majority element, it will always remain "in the lead" even after encountering another element
        Algorithm: Initialize two variables: count and candidate, set them both to 0
        Iterate through the array
        If count is 0, assign the current element as the new candidate and increment count by 1
        If the current element is the same as candidate, increment count by 1
        If the current element is different, decrement count by 1

        Explanation of Correctness:
        The algorithm works on the basis of the assumption that the majority element occurs more than n/2 times in the      array. This assumption guarantees that even if the count is reset to 0 by the other elements, the majority element will eventually regain the lead.

        Two cases: 
        1) The majority element has more than n/2 occurrences:
            The algorithm will ensure that the count remains positive for the majority element throughout the traversal, guaranteeing that it will be selected as the final candidate.

        2) If the majority element has exactly n/2 occurrences:
            In this case, there will be an equal number of occurrences for the majority element and the remaining elements combined.
            However, the majority element will still be selected as the final candidate because it will always have a lead over any other element.
        """
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num
            #count changing
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate