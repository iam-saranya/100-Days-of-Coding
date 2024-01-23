class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        ronum = ''
        i = 0
        while num > 0:
            for i in range(num // val[i]):
                ronum += syb[i]
                num -= val[i]
            i += 1
        return ronum
print(Solution().intToRoman(num))
