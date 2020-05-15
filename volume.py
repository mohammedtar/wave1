import math




Area = input( 20 )
Height = input( 10 )


Area = int(Area)
Height= int(Height)


perimeter = Area * 2 + Height * 2


perimeter = str(perimeter)

# concatention
print( + Area + Height)



square = input(2)
square = float(square)

root = math.sqrt(square)

print(root)


#Boolean Operators
boo11 = False
boo12 = True
boo13 = False



andTest = True and boo12
print(andTest)


orTest = boo11 or boo12
print(orTest)


notTest = not boo13




orderTest = not boo11 or boo13 and boo12
print(orderTest)