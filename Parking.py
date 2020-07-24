nr_test = int(input(""))

for i in range(nr_test):
    nr_shops = int(input(""))
    shops = []
    
    input_shops = input("").split(" ")
    shops = [int(shop) for shop in input_shops]
    shops.sort()

    middle = int(len(shops)/2)

    #Down
    down_distance = (shops[middle] - shops[0]) * 2
    # Up
    up_distance = (shops[-1] - shops[middle])*2

    total_distance = down_distance + up_distance

    print(total_distance)