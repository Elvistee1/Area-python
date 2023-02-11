import math
user_input = input("enter letter : ")

if user_input == 'c' :
  Radius = int(input("Enter radius : "))
  Area = math.pi * Radius**2

elif user_input == 'r' :
  height = int(input("Enter height : "))
  widht = int(input("Enter widht : "))
  Area = height * widht

else:
  Radius = int(input("Enter radius : "))
  height = int(input("Enter height : "))
  Area = math.pi * Radius**2 * height

print(Area)
