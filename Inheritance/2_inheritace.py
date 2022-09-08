from select import select


class Polygon:
    def __init__(self,sides):
        self.sides = sides
    
    def display_info():
        print("A polygon is a two dimensional shape with straight lines")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 2 edges.")
        # Polygon.display_info(self)

class Quadilateral(Polygon):
    def display_info(self):
        print("A quadilateral is a polygon with 4 edges.")  

        # super.display_info()

t1 = Triangle([5,10,15])
perimeter = t1.get_perimeter()
print("The perimeter of triangle is ",perimeter)
t1.display_info()
print()

q1 = Quadilateral([2,4,6,8])    
perimeter = q1.get_perimeter()
q1.display_info()
print("The perimeter of quadilateral is ",perimeter)

#Method overriding
# In above code, both t1.display_info and q1.display.info() invoked from Triangle Class and Quadilateral class respectively.
# This is method overriding

#To call the display_info from Base class we can do :
#   Polygon.display_info(self)     inside the trialngle or quadilateral class

#   Another method is  adding super which will automatically invoke the methos of base class as:
#  super.display_info()  herem, self is not needed inside display info because super will indicate the instance of base class.