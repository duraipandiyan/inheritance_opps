class Addition:
    def Add(self):
        a=int(input("Enter the A value:"))
        b=int(input("Enter the B value:"))
        c=a+b
        print(c)
class Subraction(Addition):
    def Sub(self):
        a = int(input("Enter the A value:"))
        b = int(input("Enter the B value:"))
        c=a-b
        print(c)

obj=Subraction()
obj.Add()
obj.Sub()
