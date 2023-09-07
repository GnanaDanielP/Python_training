class Batsman:
    def __init__(self,name,age,ipl_team):
        self.name=name
        self.age=age
        self.ipl_team=ipl_team  
        
        #child class with init function
        
class Bowler(Batsman):
    def __init__(self, name, age, ipl_team):
        super().__init__(name, age, ipl_team)
bumbra=Bowler("bumbra",30,"mumbai indian")
chahar=Bowler("chahar",28,"CSK")
print("name:",bumbra.name)
print("age:",bumbra.age)
 
print("name:",chahar.name)
print("age:",chahar.age)
print("ipl team:",chahar.ipl_team)

    
  #child class with extra function

class Captain(Batsman):
    def __init__(self, name, age, ipl_team):
        super().__init__(name, age, ipl_team)

    def dani(jerceyno):

        print("jerceyno:",jerceyno)
    dani(45)
rohit=Captain("rohit",35,"MI")
print("name:",rohit.name)
print("age:",rohit.age)
print("iplteam:",rohit.ipl_team)        
        
