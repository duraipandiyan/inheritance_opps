class myclass:   #aclass
    def inherit(self):
      self.A=int(input("enter the A value:"))
      self.B=int(input("enter the B value:"))



class Addtion(myclass):
    def add(self):
      self.inherit()
      c=self.A+self.B
      print("Addition value are",c)


class multiplication(myclass):
    def mul(self):
     self.inherit()
     c=self.A*self.B
     print("multiplication is :",c)

class subraction(myclass):
    def sub(self):
      self.inherit()
      c=self.A-self.B
      print("subraction",c)



obj1=Addtion()
obj1.add()
obj=multiplication()
obj.mul()
obj=subraction()
obj.sub()
