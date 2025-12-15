import sys

try:
    x = int(input("X: "))
    y = int(input("Y: "))
except ValueError:
   print("ERORRRR: INVALID INPUT -:")
   sys.exit(1)
   


try:
   results = x/y
except ZeroDivisionError:
   print("Error Cannot divided by zero.")
   sys.exit(1)




print(f"{x}/{y} = {results}")