from typing import List


class ThreeSum:
    def three_sum(self, nums: List[int]) -> List[list]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            if i > 1 and nums[i] == nums[i-1]:
                continue
            while left < right:
                if nums[left]+nums[right] == -nums[i]:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right += 1
                    left += 1
                    right -= 1
                elif nums[left]+nums[right] > -nums[i]:
                    right -= 1
                else:
                    left += 1
        return result


nums = [-1, 0, 1, 2, -1, -4]
sum = ThreeSum()
print(sum.three_sum(nums))
