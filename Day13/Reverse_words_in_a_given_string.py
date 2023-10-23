class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        words = s.split('.')
        reversed_words = words[::-1]
        reversed_string = '.'.join(reversed_words)
    
        return reversed_string