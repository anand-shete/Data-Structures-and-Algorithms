class Calc:
    
    def add(self, x:int, y:int):
        return x + y
    
    def sub(self, x:int, y:int):
        return x-y
    
    def mul(self, x:int, y:int):
        return self.add(x, y)
    
cal = Calc()
# ans = cal.add(3,4)
ans = cal.mul(3,2)
print(ans)