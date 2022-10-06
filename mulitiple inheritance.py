class Addition:   #class a
    def Add(self):
        a=int(input("Enter the A value:"))
        b=int(input("Enter the B value:"))
        c=a+b
        print(c)
class Subraction:   #class b
    def Sub(self):
        a = int(input("Enter the A value:"))
        b = int(input("Enter the B value:"))
        c=a-b
        print(c)
class multiple(Addition,Subraction):
    def call(self):
      self.Add()
      self.Sub()
obj=multiple()
obj.call()