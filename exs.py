class batsman:
    def name(self):
       print("name:")
       
    def age(self):
        print("age")
class bowler(batsman):
    def capno(self):
        print("capno")
b1=bowler()
# b1.name()
class fielder(batsman and bowler):
    def match(self):
        
        print("fielder")
f1=fielder()
# f1.capno()
class captain(batsman and bowler and fielder):
    def captain1(self):
        print("captain")
c1=captain()
c1.captain1()
c1.capno()
c1.name()
c1.name()
    



 
        