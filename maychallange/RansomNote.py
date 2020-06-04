"""
 Ransom Note

 Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 """
 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>magazine:
            return False
        dict={}
        for i in magazine:
            if i in dict:
                dict[i]+=1
            else:
                dict=1
        
        for char in ransomNote:
            if char not in dict:
                return False
            
            if dict[char]<=0:
                return False

            dict[i]-=1
        return True