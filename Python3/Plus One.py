class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        s = ''
        for a in digits:
            s+=str(a)
        s = str(int(s) + 1)
        ss = [int(s) for s in str(s)]
        return ss
