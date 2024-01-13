class SuperStr(str):
    def is_repeatance(self, s):
        if not s:
            return False
        return (len(self) % len(s) == 0) and (self == s * (len(self) // len(s)))

    def is_palindrom(self):
        s = self.lower()
        return s == s[::-1]


s1 = SuperStr('ababab')
print(s1.is_repeatance('ab'))
print(s1.is_repeatance('abc'))

s2 = SuperStr('RadAr')
print(s2.is_palindrom())