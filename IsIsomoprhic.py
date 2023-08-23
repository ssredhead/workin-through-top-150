class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        # all occurrences of a character must be replaced with another character
        # this must happen while preserving the order of characters
        # no two characters may map to the same character
        # but a character may map to itself
        s_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        t_dict = {}
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        
        '''
        #almost!
        map1 = []
        map2 = []

        for i in s:
            # the .index() function returns the first position of the value i
            # so we are appending the first index of where each character appears
            map1.append(s.index(i))
        for i in t:
            map2.append(t.index(i))
        #if map1 is the same as map2, that means that the positions recorded are the same, so it is isomoprophic
        return map1 == map2