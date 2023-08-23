class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        #The first thing we can do is sort the two words and check if they are equal
        return sorted(s) == sorted(t)
        '''
        #alternatively, we can increment and decrement occurances of a character in a hash map
        if len(s) != len(t):
            return False
        char_count = defaultdict(int)

        #count the frequency of characters in the first string
        for char in s:
            char_count[char] += 1

        #decrement the character from that same hash if a character occurs
        for char in t:
            char_count[char] -= 1

        #if any of the characters in the dict are non-zero, it is not an anagram
        for val in char_count.values():
            if val != 0:
                return False
        
        return True