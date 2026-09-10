# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# first line of input is list of strings strs

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.



class Solution:
    # brute force - O(N.M), O(M)
    def longest_common_prefix1(self, strs:list[int]) -> str:
        ans = strs[0]
        
        for i in range(1, len(strs)):
            curr = strs[i]
            ptr = 0
            
            for j in range(min(len(curr), len(ans))):
                if curr[j] != ans[j]:
                    break
                
                ptr += 1
                    
            ans = ans[:ptr]
            
        return ans
    
    
    # optimal brute force - O(N.M), O(1)
    def longest_common_prefix2(self, strs:list[int]) -> str:
        first = strs[0]
        
        for i in range(len(first)):
            char = first[i]
            
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return first[:i]
                
        return first
    
    
    
if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        strs = list(map(str, input().split(" ")))
        
        sol = Solution()
        # result = sol.longest_common_prefix1(strs)
        result = sol.longest_common_prefix2(strs)
        
        print(result)
        
"""
5
flower flow flight
dog racecar car
dog doggy
dog doggy diddy
cir car
"""