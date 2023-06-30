# User function Template for python3

class Solution:
    def findMissing(self, arr, n):
        d = (arr[n - 1] - arr[0]) // n
        cur = arr[0]
        for x in range(n):
            if (cur + d) == arr[x + 1]:
                cur += d
            else:
                return cur + d


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
