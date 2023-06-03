class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        ans = 0
        i = 1
        j = len(height) - 1

        lmax = height[0]
        rmax = height[-1]

        while i <= j:
            if height[i] > lmax:
                lmax = height[i]
            if height[j] > rmax:
                rmax = height[i]
            if lmax <= rmax:
                ans += lmax - height[i]
                i += 1
            else:
                ans += rmax - height[j]
                j -= 1
        return ans
