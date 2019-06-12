class cat:
    def __init__ (self):
        self.mouth = 1
        self.paws = 4
        self.eyes = 2
        
        self.toocute()

    def toocute(self):
        print ("MY BABY CAT IS TOO CUTE!")

lily = cat()
print(lily.eyes)
lily.toocute()

class boba (cat):
    def mycat(self):
        print ("My cat likes boba!")

    @staticmethod
    def Jackie():
        print("Jackie's cat is the fattest in the world because she drinks too much boba!")

bobaguys = boba()
bobaguys.mycat()
boba.Jackie()

print("i love boba")