class ArearReact:

    def __init__(self,l,b):
        self.l = l
        self.b = b

    def calculate_area(self):
        return self.l*self.b

area1 = ArearReact(5,9)
area2 = ArearReact(65,56)
print(area1.calculate_area())
print(area2.calculate_area())
