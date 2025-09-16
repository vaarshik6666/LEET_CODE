class Solution:
    def maxFreqSum(self, s: str) -> int:
        max_vowels = 0
        max_consonants = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in s:
            if i in vowels and s.count(i) > max_vowels:
                max_vowels = s.count(i)
            elif i not in vowels and s.count(i) > max_consonants:
                max_consonants = s.count(i)
        return max_vowels+max_consonants