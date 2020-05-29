class Solution:
    def rob(self, nums: List[int]) -> int:
    	a = []
    	number = len(nums)
    	if number == 0:
    		return 0
    	elif number == 1:
    		return nums[0]
    	elif number == 2:
    		return max(nums[0], nums[1])
    	a.append(nums[0])
    	a.append(max(nums[0], nums[1]))
    	for i in range(2, number):
    		a.append(max(a[i - 2] + nums[i], a[i - 1]))
    	return max(a[number - 2], a[number - 1])
