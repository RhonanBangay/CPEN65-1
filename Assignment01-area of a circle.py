# Python program that computes the area of a circle

print("Area of a Circle \n")

class area_circle:
    def __init__(self,radius,diameter):
        self.radius = radius
        self.diameter = diameter

    def area(self):
        rept = "yes"
        while rept.lower() == "yes":

            circle = input("PICK A LETTER THAT YOU WANT TO MEASURE \n A. Radius \n B. Diameter \n >>>:")

            if circle == 'A':
                self.radius = int(input("input the value of Radius: "))
                print("The area of a circle is: ", 3.14 * self.radius * self.radius, "\n")
            elif circle == 'B':
                self.diameter= int(input("input the value of Diameter: "))
                print("The area of a circle is: ", 0.25 * 3.14 * self.diameter * self.diameter, "\n")
            else:
                print("Sorry, incorrect input. \n")

            rept = input("do next computation? yes or no: ")
            print("\n")
            if rept.lower() == "no":
                break

area_circle.area(area_circle)
