class Solution:
    def twoSum(self, nums, target) -> [int]:   
        # first loop iterates a single item
        for i in range(len(nums)):
            # second loop iterates starting from after 
            # the index of the previous loop item
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]


# let's test some use cases
s = Solution()

print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([2, 7, 11, 15], 18))
print(s.twoSum([2, 7, 11, 15], 26))
print(s.twoSum([2, 7, 11, 15], 30))   
