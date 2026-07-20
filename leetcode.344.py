class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        n = len(s)
        x = n - 1

        for i in range(n):
            s[i], s[x] = s[x], s[i]
            x -= 1

            if i >= x:
                break
