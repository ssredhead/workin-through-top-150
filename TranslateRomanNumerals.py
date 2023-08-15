class Solution:
    def romanToInt(self, s: str) -> int:
        """
        #convert roman numeral to integer
        translate = []
        for char in s:
            if char == 'I':
                current = 1
            elif char == 'V':
                current = 5
            elif char == 'X':
                current = 10
            elif char == 'L':
                current = 50
            elif char == 'C':
                current = 100
            elif char == 'D':
                current = 500
            elif char == 'M':
                current = 1000
            translate.append(current)
        #next, perform the math required to get the final number
        print(translate)
        value = 0
        exceptions = [4, 9, 40, 90, 400, 900]
        for i in range(len(translate)-1):
            if (translate[i+1] - translate[i]) in exceptions:
                value += ( translate[i+1] - translate[i] )
            else:
                value += translate[i]
        return value

        Problem with the above solution - I was thinking of the addition and subtraction between neighboring 
        indices, rather than the total as a whole. The comparison is similar, but much less complicated
        """
        #first, make a dictionary of the possible options, so instead of needing
        #to translate the whole list, we can look up the corresponding value in the original list
        translate = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        #now, traverse the list by looking up the corresponding dictionary values
        #add or subtract the values according to the following rules
        # if the current value is smaller than the next value, subtract the current value from the total
        # if the current value is greater than the next value, add the current value to the total

        total = 0
        for idx in range(len(s)):
            if idx < len(s) - 1 and translate[s[idx]] < translate[s[idx+1]]: # make sure that the idx does go out of range
                total -= translate[s[idx]]
            else:
                total += translate[s[idx]]
        
        return total