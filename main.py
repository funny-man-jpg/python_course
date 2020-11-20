from shapes import *

def main():
  r = 3
  print(circle.circumference(r))
  print(circle.area(r))

if __name__ == "__name__":
  main() 

print("circle with r=3")
print("-------------------")
print("The circumference is {}".format(circle.circumference(3)))
print("The area is {}".format(circle.area(3)))
print("-------------------")
print("rectangle with w=3 and h=2")
print("-------------------")
print("The perimeter is {}".format(rectangle.perimeter(3,2)))
print("The area is {}".format(rectangle.area(3,2)))
print("-------------------")
print("square with w=4")
print("-------------------")
print("The perimeter is {}".format(square.perimeter(4)))
print("The area is {}".format(square.area(4)))
print("-------------------")
print("triangle with a=1, b=2, c=3, h=3")
print("-------------------")
print("The perimeter is {}".format(triangle.perimeter(1,2,3)))
print("The area is {}".format(triangle.area(2,4)))
print("-------------------")
print("parallelogram with a=5, b=2, h=1")
print("-------------------")
print("The perimeter is {}".format(parallelogram.perimeter(5,2)))
print("The area is {}".format(parallelogram.area(5,1)))
print("-------------------")
print("trapezoid with w=4")
print("-------------------")
print("The perimeter is {}".format(trapezoid.perimeter(4,2,5,6)))
print("The area is {}".format(trapezoid.area(6,2,4)))