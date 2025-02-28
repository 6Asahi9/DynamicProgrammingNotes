class Solution:
    def find_lcs(self, str1, str2):
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:  
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:  
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lcs = []
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:  
                lcs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:  
                i -= 1
            else:  
                j -= 1

        return "".join(reversed(lcs))

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        solution = Solution()
        lcs = solution.find_lcs(str1, str2)
        
        result = []
        i, j = 0, 0

        for c in lcs:
            while i < len(str1) and str1[i] != c:
                result.append(str1[i])
                i += 1
            while j < len(str2) and str2[j] != c:
                result.append(str2[j])
                j += 1
            result.append(c)
            i += 1
            j += 1

        result.append(str1[i:])
        result.append(str2[j:])

        return "".join(result)
