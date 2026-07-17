class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(m, n):
            if n == 0:
                return m
            else:
                return gcd(n, m%n)
        if(str1 + str2 == str2 + str1):
            gcdLen = gcd(len(str1), len(str2))
            return str1[:gcdLen]
        else:
            return ""
    