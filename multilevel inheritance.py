class Addition:   #class a
    def Add(self):
        a=int(input("Enter the A value:"))
        b=int(input("Enter the B value:"))
        c=a+b
        print("addtion value is",c)
class Subraction(Addition):   #class b
    def Sub(self):
        a = int(input("Enter the A value:"))
        b = int(input("Enter the B value:"))
        c=a-b
        print("subraction vallue is",c)
class multiplication(Subraction):
     def mul(self):
         a = int(input("Enter the A value:"))
         b = int(input("Enter the B value:"))
         c = a * b
         print("multiplication vallue is", c)
class drived(multiplication):
    def call(self):
      self.Add()
      self.Sub()
      self.mul()
obj=drived()
obj.call()