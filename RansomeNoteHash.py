class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        #since the count of the characters in magazine matter, it makes sense to use a hashmap
        dict = {}
        for char in magazine:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
        
        #now see if the characters and character count in dict is  enough to equal ransomNote
        for char in ransomNote:
            if char not in dict or dict[char] == 0:
                return False
            else:
                dict[char] -= 1
        return True
        '''

        '''
        # alternatively, you can use the "Counter" function that may or may not be built in to python
        note, mag = Counter(ransomNote), Counter(magazine)
        # next check if the intersection (probability and statistics style) of ote and mag Counter objects
        # is equal to note Counter object. If it is, then all the letters in ransomNote can be formed using magazine
        return note & mag == note
        '''

        # another solution would be to compare the count of the characters while cycling through the set of ransomNote 
        # the set means that no characters are repeated
        for char in set(ransomNote):
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True