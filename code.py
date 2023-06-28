from math import sqrt

data = []

def maths(size,data):
    mean = 0
    total = 0
    for num in data:
        mean += int(num)
    mean /= len(data)
    for x in range(len(data)):
        data[x-1] -= mean
        data[x-1] = pow(data[x-1], 2)
        total += data[x-1]
    if size == 0:
        total /= (len(data)-1)
    else:
        total /= len(data)
    return ("standard deviation = " + str(round(sqrt(total),4)))
    
def setup(data):
    inp = input("input a value ")
    if inp != "end":
        try:
            data.append(int(inp))
        except:
            print("invalid response")
            setup(data)
        else:
            setup(data)
    else:
        print("data process ended")
    while True:
        inp = input("is this a population or a sample? ").lower()
        if inp == "sample":
            print(maths(0,data))
            exit()
        elif inp == "population":
            print(maths(1,data))
            exit()
        else:
            print("invalid response")
setup(data)
