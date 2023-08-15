class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        #find the longest common prefix between all words in an array/list
        prefix = ""

        #let's try iterating through the list as if it is a 2 dimensional list (since each string can be indexed)
        for str in strs:
            for char in str:
                #stuck here because there isn't an obvious way to add and check chars like this
        '''
        #next we'll try "sorting" the list so that if there is a common prefix, it will be obvious and in the same positon
        #across all of the strings (the first and last should be checked)
        prefix = ""
        strs[:] = sorted(strs)
        print(strs)

        first_string = strs[0]
        last_string = strs[-1]
        length = min(len(first_string), len(last_string)) #use the smallest length since a prefix would only be the length of the shortest word
        for i in range(length):
            if first_string[i] != last_string[i]: #compare characters at the same positions across the words
                return prefix
            prefix += first_string[i] #if the prefix continues to match, continue to add the next character
        
        return prefix