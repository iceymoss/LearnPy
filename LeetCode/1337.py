class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0
        for v in items:
            if ruleKey == "type" and ruleValue == v[0]:
                ans += 1
            elif ruleKey == "color" and ruleValue == v[1]:
                ans += 1
            elif ruleKey == "name" and ruleValue == v[2]:
                ans += 1
        return ans