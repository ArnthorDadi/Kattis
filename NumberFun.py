n = int(input(""))

for i in range(n):
    x, y, z = input("").split(" ")
    
    x = int(x)
    y = int(y)
    z = int(z)

    if(x+y == z):
        print("Possible")
    elif(x-y == z or y-x == z):
        print("Possible")
    elif(x/y == z or y/x == z):
        print("Possible")
    elif(x*y == z):
        print("Possible")
    else:
        print("Impossible")