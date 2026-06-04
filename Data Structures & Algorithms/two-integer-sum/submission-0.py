class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        my_list = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                total = nums[i] + nums[j]
                if total == target and i != j:
                    my_list.append(i)

        return my_list

