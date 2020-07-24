n = int(input(""))

rad = {}

for i in range(n):
    color, radius = input("").split(" ")

    try: 
        radius = int(radius)
        rad[color] = radius
    except ValueError:
        color_ = radius
        radius = int(color)/2
        rad[color_] = radius

for i in range(len(rad)):
    value = min(rad.items(), key=lambda x: x[1])
    del rad[value[0]]
    print(value[0])