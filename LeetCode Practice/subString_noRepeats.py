class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        maxed = -1
        dyna = []
        for letter in s:
            if letter not in dyna:
                dyna.append(letter)
                count += 1
            else:
                if count > maxed:
                    maxed = count
                dyna = dyna[dyna.index(letter)+1:]
                count = len(dyna)+1
                dyna.append(letter)

        if count > maxed:
            maxed = count
        return maxed
