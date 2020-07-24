dit = {}
for i in range(10):
    n = int(input(""))
    value = n%42
    if((value in dit) == False):
        dit[value] = value
print(len(dit))