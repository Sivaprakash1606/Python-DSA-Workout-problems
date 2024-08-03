
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need={}
        for i in s1:
            if i in need:
                need[i]+=1
            else:
                need[i]=1

        have={}
        start,end=0,0
        while end<len(s2):
            if s2[end] not in need:
                have.clear()
                end=end+1
                start=end
                continue
            if s2[end] not in have:
                have[s2[end]]=0
            have[s2[end]]+=1
            while have[s2[end]]>need[s2[end]]:
                have[s2[start]]=have[s2[start]]-1
                start=start+1
            window=end-start+1
            if window ==len(s1):
                return True
            end=end+1
        return False
s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1,s2))