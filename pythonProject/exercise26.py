class Circle:
    pi=3.14 # class obj attribute
    # def __init__(self,radius):
    #     self.radius=radius
    #     self.pi=3.14
    def area(self,radius):
        #c_area=(self.pi * self.radius**2)
        c_area= self.pi*radius**2 # here self.pi or Circle.pi also possible
        print(c_area)
    def circumference(self,radius):
        #circum=2*self.pi*self.radius
        circum = 2 * self.pi * radius
        print(circum)

circle1=Circle()
circle1.area(5)
circle1.circumference(5)