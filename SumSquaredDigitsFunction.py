p = int(input(""))

print(int("81", 2))


for i in range(p):
    k, b, n = input("").split(" ")
    
    k = int(k)
    b = int(b)
    #n = int(n)

    summ = 0

    for number in n:
        num = int(number)**2
        
        bin_num = bin(num)[2:]
        
        while(len(bin_num) < b):
            bin_num = "0" + bin_num
    
        while(len(bin_num) > b):
            bin_num = bin_num[1:]
        
        summ += num

    print(k, summ)