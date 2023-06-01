'''
Approach:
1. Create a max_words var to keep tracking of maximum words
2. Iterate over Sentences array and use split() to convert string into list of words based on white-spaces.
3. Check whether Current sentence has more words than previous or not
'''

# Code:


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for x in sentences:
            word = x.split()
            n = len(word)
            max_words = max(max_words, n)
        return max_words
