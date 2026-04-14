class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count = {}

        for s in strs:
            freq = [0] * 26

            for c in s:
                key = ord(c) - ord('a')
                freq[key] += 1

            if tuple(freq) in count:
                count[tuple(freq)].append(s)
            else:
                count[tuple(freq)] = [s]

        res = []
        
        for keys in count.keys():
            temp = []
            for s in count[keys]:
                temp.append(s)
            res.append(temp)
        
        return res




        