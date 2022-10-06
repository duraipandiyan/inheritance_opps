class myclass:   #aclass
    def inherit(self):
      self.A=int(input("enter the A value:"))
      self.B=int(input("enter the B value:"))



class Addition(myclass):   #class b
    def add(self):
      self.inherit()
      c=self.A+self.B                        # class a,b and c hirarichal inheritance
      print("Addition value are",c)


class multiplication(myclass):     #class c
    def mul(self):
     self.inherit()
     c=self.A*self.B
     print("multiplication is :",c)


class combine(Addition,multiplication):            #d clase  act as a mulitple inheritance
    def join(self):
     self.add()
     self.mul()
obj=combine()
obj.join()
