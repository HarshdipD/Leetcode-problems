import string

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_table = dict(zip(string.ascii_lowercase, morse))
        table = str.maketrans(morse_table)
        return len(set(map(lambda x: x.translate(table), words)))
        
'''
To understand what 'maketrans' and 'translate' mean,
head over to https://www.tutorialspoint.com/python3/string_maketrans.htm
'''
