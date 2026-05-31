class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        allCharsinS = {}
        allCharsinT = {}

        for char in s:
            if char in allCharsinS:
                value = allCharsinS[char]
                allCharsinS[char] = value+1
            else:
                allCharsinS[char] = 1
        
        for char1 in t:
            if char1 in allCharsinT:
                value = allCharsinT[char1]
                allCharsinT[char1] = value+1
            else:
                allCharsinT[char1] = 1
        
        if allCharsinT == allCharsinS:
            return True
        return False