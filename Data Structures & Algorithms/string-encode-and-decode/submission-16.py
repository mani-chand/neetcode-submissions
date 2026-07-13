class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        if len(strs)==0:
            return '!@#$%^&*()'
        for stri in strs[:len(strs)-1]:
            res.append(stri+')(*&^%$#@!)')
        res.append(strs[-1])
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        if s == '!@#$%^&*()':
            return []
        return s.split(')(*&^%$#@!)')

        
