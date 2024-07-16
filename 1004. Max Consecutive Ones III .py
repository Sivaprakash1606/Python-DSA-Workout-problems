class Solution:
    def longestOnes(self, nums, k):
        main_count = 0
        count = 0
        c = 0
        for i in range(len(nums)):
            c=0
            if nums[i] == 0 :
                if c<k:
                    c = 1
                    count = 1
                else:
                    continue
            elif nums[i]==1:
                c = 0
                count = 1
            for j in range(i + 1, len(nums)):
                if nums[j]==1:
                    count+=1
                elif nums[j] == 0 and c < k:
                    c += 1
                    count += 1
                else :
                    break


            if count > main_count:
                main_count = count
        return main_count


nums =[1,1,1,0,0,0,1,1,1,1]
k = 0
print(Solution().longestOnes(nums,k))