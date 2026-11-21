class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        for i in range(1, 3):
            if i == 1:
                arr = nums[1:]
                dp_1 = [0] * (len(arr))
                dp_1[0] = arr[0]
                dp_1[1] = max(arr[0], arr[1])
                for j in range(2, len(arr)):
                    dp_1[j] = max(dp_1[j - 1], arr[j] + dp_1[j - 2])
            else:
                arr = nums[:-1]
                dp_2 = [0] * len(arr)
                dp_2[0] = arr[0]
                dp_2[1] = max(arr[0], arr[1])
                for j in range(2, len(arr)):
                    dp_2[j] = max(dp_2[j - 1], arr[j] + dp_2[j - 2])
                    
        return max(dp_1[-1], dp_2[-1])
    