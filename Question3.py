class Circle():
    def __init__(self,r,x):
        self.radius=r
        self.point=x

    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return 2*self.radius*3.14
    def appartient(self):
        if self.point==self.radius:
            print("Oui le point appartient")
        else : 
            print("Non le point n'appartient pas ")    
            
a=float(input("Donner le rayon : "))
b=float(input("Donner l'absisse du point :"))

Circle2 = Circle(a,b)
print(Circle2.area())
print(Circle2.perimeter())
Circle2.appartient()
