class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        #let's try to get the string containing only the substring
        #then compare it to the string and see if it matches. If it does, the output is true

        # subsequence = [char for char in t if s.find(char)]
        # print(subsequence)
        # if subsequence == s:
        #     return True
        # return False
        '''
        i = 0 # pointer for s
        j = 0 # pointer for t

        while i < len(s) and j < len(t): # make sure that lengths are not overflowing
            if s[i] == t[j]: # if the characters match, move the pointer for s
                i += 1
            j += 1 # move the pointer for t regardless
        return i == len(s) # if i has reached the end of s, s is a subsequence of t