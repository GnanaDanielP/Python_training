class batsman:
    def __init__(self,name,age,ipl_team):
        self.name=name
        self.age=age
        self.ipl_team=ipl_team

kohli=batsman("kohli",35,"RCB")
dhoni=batsman("dhoni",42,"CSK")
print("name:",kohli.name)
print("age:",kohli.age)
print("ipl team:",kohli.ipl_team)
print("name:",dhoni.name)
print("age:",dhoni.age)
print("ipl team:",dhoni.ipl_team)
