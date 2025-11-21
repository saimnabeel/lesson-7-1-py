
class area_of_rectanagle:
    def __init__(self,length,width):
        self.length = length
        self.width = width 
    def rectangle_area(self):
        return self.length * self.width
newrectangle = area_of_rectanagle(10,5)
print("dimensions of rectangle - length:",newrectangle.length,"width:",newrectangle.width)
print("area of rectangle:",newrectangle.rectangle_area())