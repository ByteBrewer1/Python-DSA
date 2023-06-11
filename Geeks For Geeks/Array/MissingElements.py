# User function Template for python3

class Solution:
    def findMissing(self, arr, n):
        # code here
        # Find the missing AP from arr
        diff = (arr[n-1] - arr[0]) // n
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] - arr[mid - 1] != diff:
                return arr[mid - 1] + diff
            elif arr[mid + 1] - arr[mid] != diff:
                return arr[mid] + diff
            elif mid == 0 and arr[1] - arr[0] != diff:
                return arr[0] + diff
            elif mid == n-1 and arr[n-1] - arr[n-2] != diff:
                return arr[n-1] - diff

            if arr[mid] == arr[0] + mid * diff:
                left = mid + 1
            else:
                right = mid - 1
# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMissing(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
