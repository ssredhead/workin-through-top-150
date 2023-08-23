class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        #let's try to treat this like an isomorphic word!

        #first, convert the string to a list
        string_list = list(s.split(" "))
        pattern_map = []
        word_map = []

        for char in pattern:
            pattern_map.append(pattern.index(char))
        
        for word in string_list:
            word_map.append(string_list.index(word))

        print(pattern_map)
        print(word_map)
        return pattern_map == word_map
        
        # The above definitely works, but it takes up a lot of space complexity because we are introducing
        # 3 new data structures, and a time complexity of O(n + m) which is lame

        #here is an interesting approach with a similar concept above, using set so there are no repeating elements
        # s = s.split()

        # check if the length of pattern, s, and the set of zip_longest of the two match
        # zip_longest takes two interables and prints the iterables alternatively in sequence,
        # if one iterable is printed fully, the remaining values are filled by 'None' or a final declared value
        print((set(zip_longest(pattern, s))))
        # prints something like {('a', 'dog'), ('b', 'cat')}
        # if (len(set(pattern)) == len(set(s)) == len(set(zip_longest(pattern,s)))):
        #     return True
        # else:
        #     return False
        '''
        #this can also be done with the regular zip function
        s = s.split()
        if len(pattern) != len(s): 
            return False
        return (len(set(pattern)) == len(set(s)) == len(set(zip(pattern, s))))