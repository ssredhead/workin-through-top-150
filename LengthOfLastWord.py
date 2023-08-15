class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #return the length of the last word in a string (words separated by spaces)
        strList = s.split() #slit the string by spaces into a list of the words
        return len(strList[-1]) #return the length of the last list index

        #space complexity is higher than O(1) but time complexity is O(1)