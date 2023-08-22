class Solution:
    def isPalindrome(self, s: str) -> bool:
        #TWO POINTER!
        #after getting rid of everything that isn't a letter and making everything lowercase, is it a valid palidrome?
        # s = ''.join(filter(str.isalnum, s)).lower()
        s = [char.lower() for char in s if char.isalnum()]
        return s == s[::-1] #this syntax means traverse the list from start to end, in reverse order as determined by the last parameter (-1)

        #bitwise NOT operator solution
        # s = [char.lower() for char in s if char.isalnum()] #reassign s with cleaned version
        # return all(s[i] == s[~i] for i in range(len(s)//2)) #all() checks if all parts of an iterable are true
        # using the bitwise NOT operator ~1 flips all the bit of a number, therefore making the index the negative of the 
        # index that is the parameter. Also, we only need to loop through half of the list because we are using 
        # two pointers from both ends.