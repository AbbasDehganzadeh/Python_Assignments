class Kasr:
    def __init__(self, s=0, m=0):
        """It creates new instance of Kasr class with soorat and maxraj"""
        self.s = s
        self.m = m

    def add(self, other):
        """It adds two objects of Kasr type"""
        res = Kasr()
        res.s = (self.s * other.m) + (self.m * other.s)
        res.m = self.m * other.m
        return res

    def sub(self, other):
        """It minus two objects of Kasr type"""
        res = Kasr()
        res.s = (self.s * other.m) - (self.m, other.s)
        res.m = self.m * other.m
        return res

    def mul(self, other):
        """It multiply two objects of Kasr type"""
        res = Kasr()
        res.s = self.s * other.s
        res.m = self.m * other.m
        return res

    def div(self, other):
        """It divide two objects of Kasr type"""
        res = Kasr()
        res.s = self.s * other.m
        res.m = self.m * other.s
        return res

    def show(self):
        """It shows the kasr object with neatly formatted representation"""
        print("{} / {}".format(self.s, self.m))


s1 = Kasr(2, 3)
s2 = Kasr(3, 2)

ss = s1.add(s2)
ss.show()
