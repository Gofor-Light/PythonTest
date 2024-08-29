# 27. 移除元素
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        end = len(nums) - 1
        i = 0
        while i<= end :
            if i == end:
                if nums[i] == val:
                    end = end - 1
                break
            if nums[i] == val: 
                nums[i] = nums[end]
                end = end - 1
            else:
                i = i + 1
        return end + 1
nums = [3,2,2,3]
val = 3

Solution.removeElement(None,nums,val)
print(nums)