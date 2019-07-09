class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {}
        
        for i in range(len(nums)):
        
            current_num = target - nums[i]
        
            if current_num in dict:
                return [dict[current_num],i]
            else:
                dict.update( {nums[i] : i} )