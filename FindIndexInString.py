class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        #find the start index where needle is first found in haystack if at all
        if not needle in haystack:
            return -1
        else: 
            for i in range haystack:
                for j in needle:
                if needle[j] == haystack[i]:
                    #stuck here trying to think of this as a prefix problem. There are more cases to consider
        '''

        #first take care of the edge cases
        # return -1 if len(haystack) < len(needle)
        if len(haystack) < len(needle):
            return -1
        
        #return index = if haystack and needle are 1 character and the same
        if len(haystack) == len(needle) == 1 and haystack[0] == needle[0]:
            return 0
        
        #now go through haystack for comparison purposes
        for i in range(len(haystack)):
            start = i
            j = 0

            while(haystack[i] == needle[j]):
                #if j is at the end of needle, we've found the full word and should return start
                if j == len(needle) - 1:
                    return start
                
                i += 1
                j += 1

                #if we reach the end of haystack and didn't reach the above situation, return -1
                if i == len(haystack):
                    return -1
        return -1