class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for d in operations:
            if d == "++X" or d == "X++":
                ans += 1
            elif d == "--X" or d == "X--":
                ans -= 1
        return ans