class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        if strs is None or len(strs)==0:
            return result
        if len(strs)==1:
            return strs[0]
        min_len= len(strs[0])
        for i in range(1, len(strs)): # finding the word with the least characters
            min_len= min(min_len, len(strs[i])) 
        for i in range(0, min_len): # getting the character from the 1st string
            current=strs[0][i]      # checking if the character is found in all the strings or not
            for j in range(0, len(strs)):
                if strs[j][i]!=current:
                    return result
            result=result+current
        return result
